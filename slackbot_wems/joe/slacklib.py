import time
import led
# Put your commands here
COMMAND1 = "are you awake?"
COMMAND2 = "what is your full name?"
COMMAND3 = "what is your favorite snack?"
COMMAND4 = "green led"
COMMAND5 = "what is the weather like today?" # minor test for editing straight from the web
COMMAND6 = "red led"
COMMAND7 = "blue led"

def blink_green():
	for i in range(2):
		led.green_led(1)
		time.sleep(0.2)
		led.green_led(0)
		time.sleep(0.2)

# Your handling code goes in this function
def handle_command(command):
	"""
		Determine if the command is valid. If so, take action and return
		a response, if necessary.
	"""
	response = ""

	if command.find(COMMAND1) >= 0:
		response = "Yes! It's a beautiful day!"

	elif command.find(COMMAND2) >= 0:
		response = "I have not been given one yet."

	elif command.find(COMMAND3) >= 0:
		response = "electrons!"

	elif command.find(COMMAND4) >= 0:

		if command.find("on") >= 0:
			led.green_led(1)
			response = "ok"
		elif command.find("off") >= 0:
			led.green_led(0)
			response = "ok"
		else:
			response = "I'm not sure what to do with the green led."

	elif command.find(COMMAND5) >= 0:
		response = "Sorry, I don't have that capability yet. Try asking me what the temperature is instead."


	elif command.find(COMMAND6) >= 0:

		if command.find("on") >= 0:
			led.red_led(1)
			response = "ok"
		elif command.find("off") >= 0:
			led.red_led(0)
			response = "ok"
		else:
			response = "I'm not sure what to do with the red led."

	elif command.find(COMMAND7) >= 0:

		if command.find("on") >= 0:
			led.blue_led(1)
			response = "ok"
		elif command.find("off") >= 0:
			led.blue_led(0)
			response = "ok"
		else:
			response = "I'm not sure what to do with the blue led."
            
	return response
