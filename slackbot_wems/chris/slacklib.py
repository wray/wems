# Put your commands here
COMMAND1 = "what do you think of chris?"
COMMAND2 = "say hello to your friend"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "He's goofy! :joy:"
    elif command.find(COMMAND2) >= 0:
        response = "@sirexa hello"


    return response

