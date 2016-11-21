# Put your commands here
COMMAND1 = "~~"
COMMAND2 = "name 20 breeds of dogs!"

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
        response = "black lab, yellow lab, chocolate lab, cute pug, snouser, Great Dane, terrier."
        
    return response

