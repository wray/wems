# Python package
COMMAND1 = "im a cat"

def good_cat_loop():
    # create a string to hold the response
    response = ""
    for i in range(1000):
        # Print statements do not get
        # sent back to slack, they will only
        # print out where the code is run (on the pi)
        #print("@wemmy haha")

        # Add to the response:
        response += "@wemmy good cat "

        return response
    
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response += good_cat_loop()
        
    return response

