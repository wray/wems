# Put your commands here
COMMAND1 = "haha"
COMMAND2 = "pfs"
COMMAND3 = "egg"

def haha_loop():
    # create a string to hold the response
    response = ""
    for i in range(1000):
        # Print statements do not get
        # sent back to slack, they will only
        # print out where the code is run (on the pi)
        #print("@wemmy haha")

        # Add to the response:
        response += "@wemmy haha "

    return response

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        # This next conditional is redundant, the line above already checks
        # for that exact condition
        #if command.find("haha") >= 0:

        # And because you have created a function that returns a response
        # string, just set this response to that to go back to the
        # slack channel
        response += haha_loop()

        # This would just overwrite the response, so commented out
        # response = "ok"

    elif command.find(COMMAND2) >=0:
        response = "you found an easter egg! PRO_FuZion_SlIME made this easter egg! the next easter egg command is egg"

    elif command.find(COMMAND3) >=0:
        response = "that was the last egg! i might make more!"

    return response
