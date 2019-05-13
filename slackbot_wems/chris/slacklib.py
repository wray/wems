# vim ftw

import time

import RPi.GPIO as GPIO
import emoji
#import breadBoard



# Put your commands here
COMMAND1 = "testing testing"
COMMAND2 = "roger roger"

blueLedOn = str("blue on")
blueLedOff = str("blue off")

redLedOn = str("red on")
redLedOff = str("red off")

greenLedOn = str("green on")
greenLedOff = str("green off")


GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Pin Setup
GPIO.setup(17, GPIO.OUT) # BLUE LED
GPIO.setup(27, GPIO.OUT) # RED LED
GPIO.setup(5, GPIO.OUT) # GREEN LED

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
    
    
    
    
    
    #GPIO.cleanup()
    return response

