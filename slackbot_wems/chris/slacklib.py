import time
import emoji
#import slackbot_wems.light_sensor as light
#import slackbot_wems.segment_7

#import slackbot_wems.chris.temp

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

clock = str("update clock")
scramble = str('scramble the 7')
hacker = str('hack the 7')

singleReading = str('light')

def setup():
    import RPi.GPIO as GPIO

    import slackbot_wems.chris.light as lite
    import slackbot_wems.chris.segment7 as segment
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Pin Setup
    GPIO.setup(17, GPIO.OUT) # BLUE LED
    GPIO.setup(27, GPIO.OUT) # RED LED
    GPIO.setup(5, GPIO.OUT) # GREEN LED
    GPIO.setup(22, GPIO.OUT) # YELLOW LED
    
    GPIO.setup(12, GPIO.OUT) # LDR 

setup = False

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.

    """

    if not setup:
        setup_gpio()
        setup = True

    response = ""
    if command.find(COMMAND1) >= 0:
        response = str("Surprise!")    
    elif command.find(COMMAND2) >= 0:
        response = (emoji.emojize('Python\n is\n :thumbs_up: :thumbs_up: :thumbs_up:'))

# Blue LED Commands
    elif command.find(blueLedOn) >= 0:
        GPIO.output(17, True)
        response = emoji.emojize("" + "Turning :radio_button: ON...")

    elif command.find(blueLedOff) >= 0:
        GPIO.output(17, False)
        response = emoji.emojize("" + "Turning :radio_button: OFF...")
    
# Red LED Commands
    elif command.find(redLedOn) >= 0:
        GPIO.output(27, True)
        response = emoji.emojize("" + "Turning :red_circle: ON...")

    elif command.find(redLedOff) >= 0:
        GPIO.output(27, False)
        response = emoji.emojize("" + "Turning :red_circle: OFF...")
   
# Green LED Commands
    elif command.find(greenLedOn) >= 0:
        GPIO.output(5, True)
        response = emoji.emojize("" + "Turning :green_apple: ON...")

    elif command.find(greenLedOff) >= 0:
        GPIO.output(5, False)
        response = emoji.emojize("" + "Turning :green_apple: OFF...")
   
# Yellow LED Commands
    elif command.find(yellowLedOn) >= 0:
        GPIO.output(22, True)
        response = emoji.emojize("" + "Turning :sunny: ON...")

    elif command.find(yellowLedOff) >= 0:
        GPIO.output(22, False)
        response = emoji.emojize("" + "Turning :sunny: OFF...")

# 7 Segment Commands
    elif command.find(clock) >= 0:
        print('Updating the clock!')
        response = segment.updateClock()

    elif command.find(scramble) >= 0:
        print(emoji.emojize(":egg: There is nothing better than scrambled eggs! :egg:"))
        response = segment.scramble()

    elif command.find(hacker) >= 0:
        print('Message')
        response = segment.hacker()
    
    elif command.find(singleReading) >= 0:
        a = lite.printReading()
        a = int(a)
        time.sleep(1)
        print(a)
        
        
        response = ('Here is what the LDR Sensor said to me: ' + str(a)) 

    return response

 
