import os
from slackclient import SlackClient

BOT_NAME = 'remmy'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def get_id():
    id = None
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            print(user.get('name'))
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                id = user.get('id')
    else:
        print("could not find bot user with the name " + BOT_NAME)

    return id
