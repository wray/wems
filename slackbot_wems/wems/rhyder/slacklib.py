# Put your commands here
COMMAND1 = "whats your favorite color" 
COMMAND2 = "whats your favorit food"
COMMAND3 = "whats your favorit book" 
COMMAND4 = "whats your favorit school supplies"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "green"
    elif command.find(COMMAND2) >= 0:
        response = "tacos"
    elif command.find(COMMAND3) >= 0:
        response = "mr brown can moo can you"
    elif command.find(COMMAND4) >= 0:
        response = "markers"


    return response

