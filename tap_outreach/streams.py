import singer
import pendulum

from .schemas import IDS


LOGGER = singer.get_logger()


def metrics(tap_stream_id, records):
    with singer.metrics.record_counter(tap_stream_id) as counter:
        counter.increment(len(records))


def write_records(tap_stream_id, records):
    singer.write_records(tap_stream_id, records)
    metrics(tap_stream_id, records)


class BOOK(object):
    MAILINGS = [IDS.MAILINGS, "updatedAt"]
    PROSPECTS = [IDS.PROSPECTS, "updatedAt"]
    USERS = [IDS.USERS, "updatedAt"]
    CALLS = [IDS.CALLS, "updatedAt"]
    SEQUENCES = [IDS.SEQUENCES, "updatedAt"]
    SEQUENCESTEPS = [IDS.SEQUENCESTEPS, "updatedAt"]
    SEQUENCETEMPLATES = [IDS.SEQUENCETEMPLATES]
    TEMPLATES = [IDS.TEMPLATES, "updatedAt"]

    @classmethod
    def return_bookmark_path(cls, stream):
        return getattr(cls, stream.upper())

    @classmethod
    def get_incremental_syncs(cls):
        syncs = []
        for k, v in cls.__dict__.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                if len(v) > 1:
                    syncs.append(k)

        return syncs

    @classmethod
    def get_full_syncs(cls):
        syncs = []
        for k, v in cls.__dict__.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                if len(v) == 1:
                    syncs.append(k)

        return syncs


def sync(ctx):
    for stream in ctx.selected_stream_ids:
        if stream.upper() in BOOK.get_incremental_syncs():
            bk = call_stream(ctx, stream)
            save_state(ctx, stream, bk)
        else:
            full_call(ctx, stream)


def save_state(ctx, stream, bk):
    ctx.set_bookmark(BOOK.return_bookmark_path(stream), bk)
    ctx.write_state()


def more_records(res):
    if 'links' in res and res['links'].get('next'):
        return True
    else:
        return False


def get_date_string(date):
    return pendulum.parse(date).to_date_string()


def full_call(ctx, stream):
    offset = 0

    while True:
        params = {'page[offset]': offset}

        res = ctx.client.GET(stream, params, stream)
        write_records(stream, res.get('data'))

        if more_records(res):
            offset = update_offset(res, offset)
        else:
            break


def call_stream(ctx, stream):
    ctx.update_start_date_bookmark(BOOK.return_bookmark_path(stream))
    last_updated = ctx.get_bookmark(BOOK.return_bookmark_path(stream))
    offset = 0

    while True:
        params = {'sort': 'updatedAt',
                  'page[offset]': offset,
                  'filter[updatedAt]': '{date}..{date}'.format(
                      date=get_date_string(last_updated))}

        res = ctx.client.GET(stream, params, stream)

        lastest_rec = get_last_updated(last_updated, res.get('data'))
        save_records_if_new(ctx, stream, lastest_rec, res.get('data'))

        if check_more_data(res, lastest_rec):
            offset, last_updated = update_offset_last_updated(
                res, lastest_rec, last_updated, offset)
        else:
            break

    return last_updated


def check_more_data(res, new_update):
    if more_records(res) or not_today(new_update):
        return True

    return False


def update_offset(res, offset):
    if more_records(res):
        offset += 50
    else:
        pass

    return offset


def update_offset_last_updated(res, latest_rec, last_updated, offset):
    if more_records(res):
        if get_date_string(latest_rec) != get_date_string(last_updated):
            last_updated = latest_rec
            offset = 0
        else:
            offset += 50
    elif not_today(latest_rec):
        last_updated = add_day(latest_rec)
        offset = 0
    else:
        pass

    return offset, last_updated


def save_records_if_new(ctx, stream, new_update, records):
    if new_update < ctx.get_bookmark(BOOK.return_bookmark_path(stream)):
        pass
    else:
        write_records(stream, records)


def add_day(date):
    return pendulum.parse(date).add(days=1).to_iso8601_string()


def not_today(date):
    return not pendulum.parse(date).is_today()


def get_last_updated(last_updated, records):
    for r in records:
        if r['attributes']['updatedAt'] > last_updated:
            last_updated = r['attributes']['updatedAt']

    return last_updated
