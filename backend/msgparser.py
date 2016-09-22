from re import compile


def parse_message(message):
    r = compile('(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{2}), (?P<hour>\d{2}):(?P<minutes>\d{2}) - '
                '(?P<sender>[^:]+): (?P<content>.+)')
    match = r.match(message)
    if match is not None:
        return {'year': int(match.group('year')),
                'month': int(match.group('month')),
                'day': int(match.group('day')),
                'hour': int(match.group('hour')),
                'minutes': int(match.group('minutes')),
                'sender': match.group('sender'),
                'content': match.group('content')}
    else:
        return None
