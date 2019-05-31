import os
import sys
import time
from slackclient import SlackClient

import slackbot_wems.bot_id as bot_id

# Don't introduce a dependency in the main module if it isn't required here
#import RPi.GPIO as GPIO


# Instructor imports
import slackbot_wems.wray.slacklib as wray
import slackbot_wems.joe.slacklib as joe
import slackbot_wems.chris.slacklib as chris

# Student imports
import slackbot_wems.matthew.slacklib

# WEMS imports
import slackbot_wems.wems.james.slacklib
import slackbot_wems.wems.caroline.slacklib
import slackbot_wems.wems.ibby.slacklib
import slackbot_wems.wems.rhyder.slacklib
import slackbot_wems.wems.hank.slacklib
import slackbot_wems.wems.layla.slacklib

# constants
try:
    AT_BOT = "<@" + bot_id.get_id() + ">"
except TypeError:
    pass

# instantiate client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        Need to determine an algorithm for student overloaded commands.
    """
    response = ""

    try:
        response = wray.handle_command(command)
        response += joe.handle_command(command)
        response += chris.handle_command(command)
        response += slackbot_wems.matthew.handle_command(command)

        response += slackbot_wems.wems.james.slacklib.handle_command(command)
        response += slackbot_wems.wems.hank.slacklib.handle_command(command)
        response += slackbot_wems.wems.ibby.slacklib.handle_command(command)
        response += slackbot_wems.wems.layla.slacklib.handle_command(command)
        response += slackbot_wems.wems.rhyder.slacklib.handle_command(command)
        response += slackbot_wems.wems.caroline.slacklib.handle_command(command)

    except:
        response += str(sys.exc_info()[0])

    print("["+response+"]")
    
    if len(response) == 0:
        response = "Why thank you, I don't know what else to say."
    
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    print(output_list)
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            print(command,channel)
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")



