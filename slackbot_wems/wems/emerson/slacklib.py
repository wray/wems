# Put your commands here
COMMAND1 = "mc904"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Emerson, update the response to this command by logging into GitHub and go to this link https://github.com/wray/wems/blob/master/slackbot_wems/wems/emerson/slacklib.py"
        
    return response

