# Put your commands here
COMMAND1 = "name 1 spieces of dolphin"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Bottle nose dolphin"
        
    return response

