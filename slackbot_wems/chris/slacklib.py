import time
import RPi.GPIO as GPIO
import urllib.request


COMMANDA = "are you awake?"
COMMANDB = "is tech em online?"


# Put your commands here
COMMAND1 = "blue led on"
COMMAND2 = "blue led off"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.

    """

    response = ""
    
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)

    if command.find(COMMAND1) >= 0:
        import RPi.GPIO as GPIO
        GPIO.output(17, GPIO.HIGH)
        response = "I can do that! Turning the Blue LED on..."
    
    elif command.find(COMMAND2) >= 0:
        GPIO.output(17, GPIO.LOW)
        response = "Turning off Blue LED"

    elif command.find(COMMANDB) >= 0:
        code = urllib.request.urlopen("http://www.techemstudios.com").getcode()
        if code == 200:
            response = "Tech Em Studios is currently online!"
        else:
            response = "Uh oh, it appears Tech Em Studios is offline"


    
    return response
