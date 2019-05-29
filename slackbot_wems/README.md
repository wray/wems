# WEMMY Slackbot

It's finally time! All of the students' hard work is paying off and the WEMMY Slackbot is under way.

## What is a Slackbot
We've touched on what a Slackbot is during class; a Slackbot is a chatbot, that is, a robot for chatting!

## How does it work?
The Slackbot has been programmed using a host of different Python files to take any command created by students and provide a corresponding output.

* For instance, the input `james is the best`

* Produces the output `you are the best then everyone especially Alex`)

The underlying code magic behind our Slackbot, involves APIs and lots, lots more!

## How does the code work
The code works through multiple files, in our case: `bot_id.py`, `slackpi.py`, `testit.py`, and an initialization file: `__init__.py`

Each file calls back to the others, `slackpi.py` is the bread and butter of the whole operation however and includes much of the backbone of the whole bot.

As for how each student produces their commands:
* Each student has their own unique AWS Cloud9 Environment that is connected to a shared GitHub repository.
* This GitHub repository contains a folder for each student, with each folder containing a unique `slacklib.py` file, the code for which looks like this:
``` python
# Put your commands here
COMMAND1 = ""
COMMAND2 = ""
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = ""
    elif command.find(COMMAND2) >= 0:
        response = ""

    return response
```
* It is here where a student can first create the phrase for their command and then define what happens when it is issued.
