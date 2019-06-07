# Wremmy Slackbot

[![Build Status](https://travis-ci.org/wray/wems.svg?branch=master)](https://travis-ci.org/wray/wems)

### Introduction

The **Wremmy Slackbot** is a project that was created and developed during an _after school enrichment_ class at WEMS. The goal of the Slackbot was to teach the students various Computer Science and programming concepts, and get them more comfortable with Python. Not only did they have to type their code, but they also had to commit it to a class repository. 

This allowed the chance for them to see how real teams collaborate on software, and how everyone's changes are tracked throughout the development life cycle. Once they had committed their changes, TravisCI would pick those new changes up, run tests, and if passed deploy a new version of the PyPi package.

Finally a cronjob was running every five minutes on a Raspberry Pi that would grab the newest version of the PyPi package, update, and rerun it on the Raspberry Pi. That latest version that was just downloaded would have the kids new commands that they just committed a couple minutes ago!

The first part of this `README.md` just focues on what is needed to run the Slackbot software locally on your own computer, with your own Slack channel configured. 

---

- [Wremmy Slackbot](#wremmy-slackbot)
    - [Introduction](#introduction)
  - [Preparation](#preparation)
    - [Slack](#slack)
    - [Clone The Repository](#clone-the-repository)
    - [Install Python](#install-python)
    - [Dependencies](#dependencies)
  - [Setup](#setup)
    - [Adding API key to `slackbotctl`](#adding-api-key-to-slackbotctl)
    - [Changing the `BOT_NAME`](#changing-the-bot_name-variable)
  - [Running Slackbot](#running-slackbot)
    - [Ready, Set, Go!](#ready-set-go)
  - [Adding Your Own Commands](#adding-your-own-commands)
    - [Create a new folder](#create-a-new-folder)
    - [Add some files](#add-some-files)
    - [Edit `slacklib.py`](#edit-slacklibpy)
    - [Edit `slackpi.py`](#edit-slackpipy)


## Preparation

### Slack

1. Create a new Slack channel
2. Navigate to the admin settings at `channel-name.slack.com/admin`
3. Grab the API key

### Clone The Repository

You will need to download the repository. There are two ways to do this, either by downloading the zip file from the Web UI, or by using the `git clone` command.

Once downloaded, navigate to where you have saved it via the Terminal

### Install Python

Currently this project requires `Python 3.5`

```sh
apt-get install python3 python3-pip
```

### Dependencies

`pip install --user slackclient emoji RPi.GPIO Adafruit_LED_Backpack Adafruit_DHT`

## Setup

### Adding API key to `slackbotctl`

In the `slackbotctl` file on line 8:

```bash
export SLACK_BOT_TOKEN=${your_slack_bot_token}
```

You want to remove `${your_slack_bot_token}` and input your own API key surrounded by quotes like this:

```bash
export SLACK_BOT_TOKEN='my-api-key'
```

### Changing the `BOT_NAME` variable

Within the file `slackbot_wems/bot_id.py` there is a variable that is declared called `BOT_NAME`. You will need to change this value to match whatever it is you have named your Slackbot within the admin settings of your channel

```python
BOT_NAME = 'whatever-you-named-your-bot'
```

## Running Slackbot

### Ready, Set, Go!

In order to start the Slackbot, you will run the script `slackbotctl`. First though we have to make the script executable:

```sh
chmod +x slackbotctl
```

This can be done by opening up your Terminal, navigating to the folder that the script is located and typing:

```sh
./slackbotctl
```

If the script runs with no errors, you should see output of the Slack channel streaming down your Terminal.

## Adding Your Own Commands

### Create a new folder

In order to add your own commands to the Slackbot you should start with making your own folder within the `slackbot_wems` folder 

### Add some files

Inside your newly created folder create two files:

- `__init__.py`
- `slacklib.py`

### Edit `slacklib.py`

Here is some starter code: 

```python
# Put your commands here
COMMAND1 = " "
COMMAND2 = " "
COMMAND3 = " "

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "This is what I will say if you type in the value for COMMAND1"
    if command.find(COMMAND2) >= 0:
        response = "This is what I will say if you type in the value for COMMAND2"
    if command.find(COMMAND3) >= 0:
        response = "This is what I will say if you type in the value for COMMAND3"

    return response
```

### Edit `slackpi.py`

Once you have finished adding your commands and saved your work you need to move over to the `slackbot_wems/slackpi.py` file and add a line of code so that Python knows where to find your newly created commands!

Add this towards to top near the other `import` lines:

```python
import slackbot_wems.folder-name.slacklib
```

And scroll down a bit you will see a bunch of lines starting with the word `response`. Add a line like this so that Python pick up your commands:

```python
response += folder-name.handle_command(command)
```

Alright! You should be ready to rock, and test our your new commands.

Try to run the Slackbot again:

```sh
./slackbotctl
```

At this point you should have up and running a basic Slackbot. Your Slackbot is listening to the output of whatever Slack channel you have invited them into. Whenever they hear one of the commands you added, it will respond with what you have programmed it to respond with! Pretty cool, huh?
