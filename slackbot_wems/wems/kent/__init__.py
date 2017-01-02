# Python package
COMMAND1 = "im a cat"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        for i in range (145):
            response = "good cat"
        
    return response

