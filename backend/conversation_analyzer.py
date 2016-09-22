
from os import remove, listdir, makedirs
from os.path import exists
from re import compile
from datetime import datetime, timedelta
from msgparser import parse_message

filename = 'chat.txt'
dirname = 'conversations'
cooldown_period = timedelta(hours=1)


def log(conversations):
    if exists(dirname):

        #   delete previous logs

        r = compile('conversation\d{1,}.txt')
        for file in listdir(dirname):
            if r.match(file) is not None:
                remove('{}/{}'.format(dirname, file))

    # create new logs

    if not exists(dirname):
        makedirs(dirname)

    logfilename_template = '{}/conversation{}.txt'
    for index, conversation in enumerate(conversations):
        logfilename = logfilename_template.format(dirname, index)
        with open(logfilename, 'w', encoding='utf-8') as logfile:
            logfile.writelines(conversation)


def analyze_chat_file():
    with open(filename, 'r', encoding='utf8') as chatfile:
        messages = chatfile.readlines()
        conversations = []
        base_msg = messages[0]
        conversation = [base_msg]
        for msg in messages[1:]:
            msg_data1 = parse_message(base_msg)
            msg_data2 = parse_message(msg)
            if msg_data2 is not None:
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

        log(conversations)
        return conversations


def load_conversations():
    conversations = []
    r = compile('conversation\d{1,}.txt')
    for file in listdir(dirname):
        if r.match(file) is not None:
            with open('{}/{}'.format(dirname, file), 'r', encoding='utf-8') as logfile:
                conversations += [logfile.readlines()]
    return conversations