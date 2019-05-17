import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 12

def getReading(pin):
    count = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(pin, GPIO.IN)
    
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
     
    return count
    

def printReading():
    
    return getReading(12)


