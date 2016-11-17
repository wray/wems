# Put your commands here
COMMAND1 = "hi"
COMMAND2 = "temp?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Hi Minecraftman"
    
    elif command.find(COMMAND2) >= 0:
        response = "60F"     
        
    return response

