# Put your commands here
COMMAND1 = "who is your sister"
COMMAND2 = "what are you doing for the talent show"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    # RESPONSE TO COMMAND1
    if COMMAND1 in command:
        response = "naomi test passed!"
    
    # RESPONSE TO COMMAND2
    elif COMMAND2 in command:
		response = "gymnstics, drawing or magic"
        
    return response

