import json
import jsonlines

# This function loads messages from a json file. I used a Skype exports json file.
def load_messages():

    messages = open('messages.json',)
    messages = json.load(messages)
    message_list = messages['conversations'][0]['MessageList']
    
    return message_list

    # len_conversations = len(messages['conversations'])
    # conversations = messages['conversations']
    # all_conversations = [d['displayName'] for d in messages['conversations']]
    # for i in range(len(conversations)):
    #     print(len(conversations[i]['MessageList']))
    #     print(conversations[i]['displayName'])

# This function builds a list of query/response pairs from the list of messages
def build_Yenachi_convos():
    message_list = load_messages()
    len_messages = len(message_list)
    list_of_Yenachi_convos = []
    
    #Clean data. Removing text representations of images/hlinks/quotes/refs
    bad_phrases = ['URI', 'addmember', 'partlist', 'timestamp', 'href', '<at id=', '<ss']
    i = 0
    while (i < len_messages - 1):
        message = message_list[i]
        if message['displayName'] == 'Yenachi':
            previous_message = message_list[i + 1]
            convo_pair = []
            response = message['content']

            # combine all continuous messages from Yenachi
            while(previous_message['displayName'] == 'Yenachi'):
                response += ". " + previous_message['content']
                i += 1
                previous_message = message_list[i + 1]

            #Add separator to help model
            convo_pair.append(previous_message["content"] + '\n\n###\n\n')

            #Add whitespace & stop symbol to help model
            convo_pair.append(' ' + response + '***')

            #Check if message contains image/quote/emoji/other Skype jargon
            illegal_message = False
            for phrase in bad_phrases:
                if phrase in convo_pair[0] or phrase in convo_pair[1]:
                    illegal_message = True

            if illegal_message == False:
                list_of_Yenachi_convos.append(convo_pair)
        i += 1
    return list_of_Yenachi_convos

#This function builds a formatted jsonl file for GPT training
def build_json_list():
    convos = build_Yenachi_convos()
    jsonl_formatted_convos = []
    for i in convos:
        message, response = i
        dict_pair = {
            'prompt': message,
            'completion': response
        }
        jsonl_formatted_convos.append(dict_pair)

    with jsonlines.open('message_pairs.jsonl', 'w') as writer:
        writer.write_all(jsonl_formatted_convos)

#This function checks how many messages each person has sent in the group chat
def convos_per_person():
    message_list = load_messages()
    len_messages = len(message_list)
    displayNames = []
    chanel_count = 0
    print(len_messages)
    for i in range(len_messages - 1):
        message = message_list[i]
        # if message['displayName'] not in displayNames:
        #     displayNames.append(message['displayName'])
        if message['displayName'] == None:
            chanel_count += 1
    print(chanel_count)
# if name == '__main__':
#     build_json_list()
