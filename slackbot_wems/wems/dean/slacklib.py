# Put your commands here
COMMAND1 = "~~"
COMMAND2 = "how do we fix the rollercoaster?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Huh?"
    elif command.find(COMMAND2) >= 0:
        response = "let's buy new rails and put them on!"
        
    return response

