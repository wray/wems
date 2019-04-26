# Put your commands here
COMMAND1 = "is techem boring when weget pizza"
COMMAND2 = "do you like jakc a lantern"
COMMAND3 = "what is your favorit my little ponny charicter"
COMMAND4 = "chickin"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "no.i love pizza"
    elif command.find(COMMAND2) >= 0:
        response = "yes"
    elif command.find(COMMAND3) >= 0:
        response = "i doint like my little ponny."
    elif command.find(COMMAND4) >= 0:
        response = "what!"


    return response

