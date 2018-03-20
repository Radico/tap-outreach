import requests
from singer import metrics
import backoff

BASE_URL = "https://api.outreach.io/api/v2/"


class RateLimitException(Exception):
    pass


def _join(a, b):
    return a.rstrip("/") + "/" + b.lstrip("/")


class Client(object):
    def __init__(self, config):
        self.user_agent = config.get("user_agent")
        self.access_token = config.get("access_token")
        self.session = requests.Session()

    def prepare_and_send(self, request):
        if self.user_agent:
            request.headers["User-Agent"] = self.user_agent

        request.headers["Content-Type"] = "application/vnd.api+json"
        request.headers["Accept"] = "application/vnd.api+json"

        request.headers["Authorization"] = "Bearer %s" % self.access_token

        return self.session.send(request.prepare())

    def url(self, path):
        return _join(BASE_URL, path)

    def create_get_request(self, path, params):
        return requests.Request(method="GET", url=self.url(path),
                                params=params)

    @backoff.on_exception(backoff.expo,
                          RateLimitException,
                          max_tries=10,
                          factor=2)
    def request_with_handling(self, request, tap_stream_id):
        with metrics.http_request_timer(tap_stream_id) as timer:
            response = self.prepare_and_send(request)
            timer.tags[metrics.Tag.http_status_code] = response.status_code
        if response.status_code in [429, 503]:
            raise RateLimitException()
        response.raise_for_status()
        return response.json()

    def GET(self, path, params, *args, **kwargs):
        req = self.create_get_request(path, params)
        return self.request_with_handling(req, *args, **kwargs)
