# Put your commands here
COMMAND1 = "do you like pokemon"
COMMAND2 = "how are you"
# COMMAND3 = ""
# COMMAND5 = ""
# Your handling de goes in this function

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "Maybe. Do YOU like pokemon?"
    if COMMAND2 in command:
		response = "no, how are you?"
    
 
 
        
    return response

