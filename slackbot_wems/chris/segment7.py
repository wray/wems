# A tiny library to do fun things with the 7 Segment display from Adafruit
#
# Developed by Tech Em Labs

import time
import random
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

def clear():
	segment.clear()
	segment.write_display()


def randomOdds():
	segment.clear()
	 
	segment.set_digit(0,random.randint(0,9))
	segment.set_digit(1,random.randint(0,9))
	segment.set_digit(2,random.randint(0,9))
	segment.set_digit(3,random.randint(0,9))
	
	segment.write_display()
	time.sleep(0.25)

#randomOdds()


def scramble():
	for i in range(20):
		segment.clear() 
		segment.set_digit(0,random.randint(0,9))
		segment.set_digit(1,random.randint(0,9))
		segment.set_digit(2,random.randint(0,9))
		segment.set_digit(3,random.randint(0,9))
	
		segment.write_display()
		time.sleep(0.25)

#scramble()

def hacker():
	for i in range(50):
		segment.clear() 
		segment.set_digit(0,random.randint(0,1))
		segment.set_digit(1,random.randint(0,1))
		segment.set_digit(2,random.randint(0,1))
		segment.set_digit(3,random.randint(0,1))
	
		segment.write_display()
		time.sleep(0.10)

#hacker()

def updateClock():
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second

	segment.clear()

	segment.set_digit(0, int(hour / 10))
	segment.set_digit(1, hour % 10)
	segment.set_digit(2, int(minute / 10))
	segment.set_digit(3, minute % 10)

	segment.set_colon(second % 2)

	segment.write_display()

	time.sleep(0.25)

#updateClock()
