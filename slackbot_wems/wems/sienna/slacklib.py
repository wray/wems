# Put your commands here
COMMAND1 = "name a venomous snake"
COMMAND1 = "name a school"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Indian cobra???"
    elif command.find(COMMAND1) >= 0:
        response = "wems"
        
    return response

