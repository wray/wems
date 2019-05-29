# vim ftw

import time

import emoji

# For local testing
#import light_sensor as light
#import segment_7

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
#quadReading = str('more readings')

#showTemp = str('show me the temp')

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
   
    #elif command.find(quadReading) >= 0:
        #a = []
        #for i in range(5):
            #a.append(lite.printReading())
            #time.wait(.5)
        
        #print(a)
        #response = ('More light: ' + (a))
    elif command.find(showTemp) >= 0:
        
        response = fuck.read_temp_humidity()
        #response = ('The current temp is %0.2f C, %0.2f F, with a humidty of %0.2f%%' % (read_temp_humidity()))
    


    return response

 
