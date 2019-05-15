# vim ftw

import time

import RPi.GPIO as GPIO
import emoji

# For local testing
#import light_sensor as light
#import segment_7

import slackbot_wems.chris.light_sensor
import slackbot_wems.chris.segment7 as segment

# Put your commands here
COMMAND1 = "testing testing"
COMMAND2 = "roger roger"

blueLedOn = str("blue on")
blueLedOff = str("blue off")

redLedOn = str("red on")
redLedOff = str("red off")

greenLedOn = str("green on")
greenLedOff = str("green off")

yellowLedOn = str("yellow on")
yellowLedOff = str("yellow off")

lightAverage = str("the light")

clock = str("update clock")
scramble = str('scramble the 7')
hacker = str('hack the 7')



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin Setup
GPIO.setup(17, GPIO.OUT) # BLUE LED
GPIO.setup(27, GPIO.OUT) # RED LED
GPIO.setup(5, GPIO.OUT) # GREEN LED
GPIO.setup(22, GPIO.OUT) # YELLOW LED

GPIO.setup(12, GPIO.OUT) # LDR 

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.

    """

    response = ""
    if command.find(COMMAND1) >= 0:
        response = str("Surprise!")    
    elif command.find(COMMAND2) >= 0:
        response = (emoji.emojize('Python\n is\n :thumbs_up: :thumbs_up: :thumbs_up:'))
    
    
    # Breadboard Commands

    # BLUE LED
    elif command.find(blueLedOn) >= 0:
        GPIO.output(17, True)
        #breadBoard.blueLed(1)
        response = emoji.emojize("" + "Turning :radio_button: ON...")

    elif command.find(blueLedOff) >= 0:
        GPIO.output(17, False)
        #breadBoard.blueLed(0)
        response = emoji.emojize("" + "Turning :radio_button: OFF...")
    
    # RED LED  
    elif command.find(redLedOn) >= 0:
        GPIO.output(27, True)
        #breadBoard.blueLed(1)
        response = emoji.emojize("" + "Turning :red_circle: ON...")

    elif command.find(redLedOff) >= 0:
        GPIO.output(27, False)
        #readBoard.blueLed(0)
        response = emoji.emojize("" + "Turning :red_circle: OFF...")
   
   # GREEN LED
    elif command.find(greenLedOn) >= 0:
        GPIO.output(5, True)
        #breadBoard.greenLed(1)
        response = emoji.emojize("" + "Turning :green_apple: ON...")

    elif command.find(greenLedOff) >= 0:
        GPIO.output(5, False)
        #readBoard.blueLed(0)
        response = emoji.emojize("" + "Turning :green_apple: OFF...")
   
   # YELLOW LED

    elif command.find(yellowLedOn) >= 0:
        GPIO.output(22, True)
        #breadBoard.greenLed(1)
        response = emoji.emojize("" + "Turning :sunny: ON...")

    elif command.find(yellowLedOff) >= 0:
        GPIO.output(22, False)
        #readBoard.blueLed(0)
        response = emoji.emojize("" + "Turning :sunny: OFF...")

    #elif command.find(lightAverage) >=0:


    elif command.find(clock) >= 0:
        print('Updating the clock!')
        response = segment.updateClock()

    elif command.find(scramble) >= 0:
        print emoji.emojize(':egg: There is nothing better than scrambled eggs! :egg:')
        response = segment.scramble()

#GPIO.cleanup()
    return response

 
