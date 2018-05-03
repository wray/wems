# Put your commands here
COMMAND1 = "name a venomous snake"
COMMAND2 = "name a school"
COMMAND3 = "what is the weather?"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "Indian cobra???"
    elif COMMAND2 in command:
        response = "wems"
    elif COMMAND3 in command:
		response = "Look outside!"
        
    return response

