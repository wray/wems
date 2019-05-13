import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 12

def light(pin):
    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)

    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
    
    return count

#avg = light(pin)
#print(avg)
'''try:
    avg = []
    for i in range(24)
        avg.append(light(pin))

    del avg[0:4]

    avg = sum(avg) / len(avg)

    print(avg)'''
