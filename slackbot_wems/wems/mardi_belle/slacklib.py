# Put your commands here
COMMAND1 = "mardi belle test"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "mardi belle test passed!"
        
    return response

