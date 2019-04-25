# Put your commands here
COMMAND1 = "name 1 spieces of dolphin"
COMMAND2 = "whats my favorite candy"
COMMAND3 = "name my favorite breed of dog"
COMMAND4 = "what do i like" 




# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Bottlenose dolphin"

    elif command.find(COMMAND2) >= 0:
        response = "sour patch kids"
   
    elif command.find(COMMAND3) >= 0:
         response = "corgi"
    elif command.find(COMMAND4) >= 0:
         
         response = "doughnut"
        
    return response
