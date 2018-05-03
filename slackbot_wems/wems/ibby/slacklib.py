# Put your commands here
COMMAND1 = "ibby test"
COMMAND2="hi"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "ibby test passed!"
    if COMMAND2 in command:
		response = "stinky shoes"
    return response

