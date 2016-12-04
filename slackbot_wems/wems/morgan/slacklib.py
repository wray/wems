# Put your commands here
COMMAND1 = "it is a mammal"
COMMAND2 = "name 20 breeds of dogs!"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "poodle pug blodhound foxhound buldog chcocolatelab grayhound golden retriever chihuahua mastiff newfoundland sheepdog shih tzu that is all i know."
    elif command.find(COMMAND2) >= 0:
        response = "black lab, yellow lab, chocolate lab, cute pug, schnauzer, Great Dane, terrier, poodle, pug, blodhound, foxhound, buldog, chcocolatelab, grayhound, golden retriever, chihuahua, mastiff, newfoundland, sheepdog, shih."
        
    return response

