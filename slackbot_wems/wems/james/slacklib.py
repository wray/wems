# Put your commands here
COMMAND1 = " james is the best"
COMMAND2 = " is techem cool"
COMMAND3 = "i fell bab that everone get pizza"
COMMAND4 = " i mad at ever who this lough"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "you are the best then every one especially Alex"
    elif command.find(COMMAND2) >= 0:
        response = "no"
    elif command.find(COMMAND3) >= 0:
        response = "i am so mad at pizza"
    elif command.find(COMMAND4) >= 0:
        response = " great" 


    return response

