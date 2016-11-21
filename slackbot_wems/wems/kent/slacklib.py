# Put your commands here
COMMAND1 = "hi"
COMMAND2 = "temp?"
COMMAND3 = "am i a hacker?"
COMMAND4 = "who is the master"

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
    elif command.find(COMMAND3) >= 0:
        response = "yes, you are destined to be a hacker"
    elif command.find(COMMAND4) >= 0:
        response = "Kent is the master, all hail Kent" 
            
        
    return response
