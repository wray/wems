# Put your commands here
COMMAND1 = "get me a toilet"
COMMAND2 = "get me a lot of money. "
COMMAND3 = "black tree"
COMMAND4 = "a face."
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "ok ill get you a toilet"
    elif command.find(COMMAND2) >= 0:
        response = "ok, i'll get you 10000000000000000000066665555577778888888886666666666999999999000000000002222222333333444 dollars"
    elif command.find(COMMAND3) >= 0:
        response = "what"
    elif command.find(COMMAND4) >= 0:
        response = "i don`t understand."
    return response

