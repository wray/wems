# Put your commands here
COMMAND1 = "What do you think of Chris?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "He's goofy! :joy:"
        
    return response

