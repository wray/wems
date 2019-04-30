import os
import sys
import time
from slackclient import SlackClient

import bot_id

import RPi.GPIO as GPIO

# Instructor imports
import wray.slacklib
import joe.slacklib
import chris.slacklib

# Student imports  
import matthew.slacklib

# WEMS imports
import wems.james.slacklib
import wems.caroline.slacklib
import wems.ibby.slacklib
import wems.rhyder.slacklib
import wems.hank.slacklib
import wems.layla.slacklib

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

    import RPi.GPIO as GPIO

    try:
        response = wray.slacklib.handle_command(command)
        response += joe.slacklib.handle_command(command)
        response += chris.slacklib.handle_command(command)
    
        response += matthew.slacklib.handle_command(command)

        response += wems.james.slacklib.handle_command(command)
        response += wems.hank.slacklib.handle_command(command)
        response += wems.ibby.slacklib.handle_command(command)
        response += wems.layla.slacklib.handle_command(command)
        response += wems.rhyder.slacklib.handle_command(command)
        response += wems.caroline.slacklib.handle_command(command)

    except:
        response += str(sys.exc_info()[0])

    print("["+response+"]")
    
    if len(response) == 0:
        response = "Why thank you, I don't know what else to say."
    
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    
    import RPi.GPIO as GPIO
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



