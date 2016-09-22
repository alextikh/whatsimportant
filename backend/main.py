
from operator import itemgetter
from msgparser import parse_message
from conversation_analyzer import analyze_chat_file, load_conversations


num_top_members = 5
username = 'ERIC'


def find_top_members(conversations):
    members = {}
    for index, conversation in enumerate(conversations):
        for msg in conversation:
            msg_data = parse_message(msg)
            sender = msg_data['sender']
            if sender in members:
                if 'conversation{}'.format(index) not in members[sender]:
                    members[sender] += ['conversation{}'.format(index)]
            else:
                members[sender] = ['conversation{}'.format(index)]
    members = sorted(members.items(), key=lambda x: len(x[1]), reverse=True)
    if len(members) <= num_top_members:
        return members
    else:
        return members


def find_top_members1(messages):
    members = {}
    for msg in messages:
        msg_data = parse_message(msg)
        if msg_data is not None:
            sender = msg_data['sender']
            if sender in members:
                members[sender] += 1
            else:
                members[sender] = 1
    members = sorted(members.items(), key=itemgetter(1), reverse=True)
    if len(members) <= num_top_members:
        return members
    else:
        return members





def find_user_conversations(conversations):
    participated = []

    for index, conversation in enumerate(conversations):
        for msg in conversation:
            msg_data = parse_message(msg)
            sender = msg_data['sender']
            if sender == username:
                participated += [index]
                break
    return participated


def match_members(conversations):
    matches = {}
    participated = find_user_conversations(conversations)
    for index in participated:
        matches[index] = []
        for msg in conversations[index]:
            msg_data = parse_message(msg)
            sender = msg_data['sender']
            if sender not in matches[index]:
                matches[index] += [sender]

    return matches


def main():
    # conversations = analyze_chat_file()
    conversations = load_conversations()
    print(len(conversations))


if __name__ == '__main__':
    main()