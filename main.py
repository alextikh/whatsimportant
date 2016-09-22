from re import compile
from datetime import datetime, timedelta

from os import remove, listdir

filename = 'chat.txt'
cooldown_period = timedelta(hours=1)
num_top_members = 5

def parse_message(message):
    r = compile('(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{2}), (?P<hour>\d{2}):(?P<minutes>\d{2}) - '
                '(?P<sender>[^:]+): (?P<content>.+)')
    match = r.match(message)
    if match != None:
        return {'year': int(match.group('year')),
                'month': int(match.group('month')),
                'day': int(match.group('day')),
                'hour': int(match.group('hour')),
                'minutes': int(match.group('minutes')),
                'sender': match.group('sender'),
                'content': match.group('content')}
    else:
        return None


def split_conversations(messages):
    conversations = []
    base_msg = messages[0]
    conversation = [base_msg]
    for msg in messages[1:]:
        msg_data1 = parse_message(base_msg)
        msg_data2 = parse_message(msg)
        if msg_data2 != None:
            msg_d1 = datetime(year=msg_data1['year'], month=msg_data1['month'], day=msg_data1['day'],
                              hour=msg_data1['hour'], minute=msg_data1['minutes'])
            msg_d2 = datetime(year=msg_data2['year'], month=msg_data2['month'], day=msg_data2['day'],
                              hour=msg_data2['hour'], minute=msg_data2['minutes'])
            if msg_d2 - msg_d1 < cooldown_period:
                conversation += [msg]
                base_msg = msg
            else:
                conversations += [conversation]
                base_msg = msg
                conversation = [base_msg]
    return conversations


def find_top_members(messages):
    members = {}
    for msg in messages:
        msg_data = parse_message(msg)
        sender = msg_data['sender']
        if sender in members:
            members[sender] += 1
        else:
            members[sender] = 1
    members = sorted(members.items(), key=lambda x: x[])


def log(conversations):
    #   delete previous logs

    r = compile('conversation\d{1,}.txt')
    for file in listdir('.'):
        if r.match(file) != None:
            remove(file)

    # create new logs

    logfilename_template = 'conversation{}.txt'
    for (index, conversation) in enumerate(conversations):
        logfilename = logfilename_template.format(index)
        with open(logfilename, 'w', encoding='utf-8') as logfile:
            logfile.writelines(conversation)

def main():
    with open(filename, 'r', encoding='utf8') as chatfile:
        messages = chatfile.readlines()
        conversations = split_conversations(messages)
        log(conversations)


if __name__ == '__main__':
    main()
