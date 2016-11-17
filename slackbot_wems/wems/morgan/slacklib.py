# Put your commands here
COMMAND1 = "what is a bambat" 
COMMAND2 = "name 20 breeds of dog" 
# https://gist.github.com/0affa3090cceef3cd7e52d6cd72e94e9https://
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "it is a mammal" 
    elif command.find(COMMAND2) >=0:
        response = "poodle pug blodhound foxhound buldog chcocolatelab grayhound golden retriever chihuahua mastiff newfoundland sheepdog shih tzu that is all i know" 


    
    return response

