# Put your commands here
COMMAND1 = "haha"
COMMAND2 = "pfs"
COMMAND3 = "egg"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "@wemmy haha"
    elif command.find(COMMAND2) >=0:
        response = "you found an easter egg! PRO_FuZion_SlIME made this easter egg! the next easter egg command is egg"
        
    elif command.find(COMMAND3) >=0:
        response = "that was the last egg! i might make more!"
        
    return response

