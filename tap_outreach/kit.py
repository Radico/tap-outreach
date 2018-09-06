from tap_kit import TapExecutor, BaseClient, main_method
from tap_kit.utils import (
    date_to_date_str, transform_write_and_count
)

import requests

from .streams_kit import STREAMS

REQUIRED_CONFIG_KEYS = ["start_date", "access_token", "refresh_token",
                        "client_id", "client_secret", "redirect_uri"]


class OutreachTap(TapExecutor):
    url = "https://api.outreach.io/api/v2/"
    pagination_type = 'next'
    replication_key_format = 'datestring'
    res_json_key = 'data'
    auth_type = 'oauth'

    def get_latest_for_next_call(self, records, replication_key, last_updated):
        for r in records:
            if r['attributes']['updatedAt'] > last_updated:
                last_updated = r['attributes']['updatedAt']

        return last_updated

    def build_params(self, stream, last_updated, offset=0):

        return {'sort': 'updatedAt',
                'page[offset]': offset,
                'filter[updatedAt]': '{date}..{date}'.format(
                    date=date_to_date_str(last_updated))}

    def should_write(self, records, stream, last_updated):
        if last_updated < stream.get_bookmark():
            pass
        else:
            transform_write_and_count(stream, records)

    def update_creds(self, creds):
        for key in creds:
            self.config[key] = creds[key]

    def refresh_creds(self):
        creds = self.config

        data = {'client_id': creds['client_id'],
                'client_secret': creds['client_secret'],
                'redirect_uri': creds['redirect_uri'],
                'grant_type': 'refresh_token',
                'refresh_token': creds['refresh_token']
                }

        res = requests.post(url='https://api.outreach.io/oauth/token',
                            data=data)

        creds = {'access_token': res.json()['access_token'],
                 'refresh_token': res.json()['refresh_token']}

        self.update_creds(creds)

        return creds

    def build_headers(self):
        self.refresh_creds()

        return {
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
            "Authorization": "Bearer %s" % self.config.get('access_token')
        }


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        OutreachTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
