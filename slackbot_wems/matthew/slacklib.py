# Put your commands here

COMMAND1 = "who is sirtomato"
COMMAND2 = "talk in binary"
COMMAND3 = "i dont like you"
COMMAND4 = "brit"
COMMAND5 = "h@ck3r_1if3"
COMMAND6 = "promote"


# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """

    response = ""
    if command.find(COMMAND1) >= 0:
        response = "A cuber/coder that loves Arch Linux and tiling window managers."
    elif command.find(COMMAND2) >= 0:
        response = """01000111 01101111 00100000 01100001 01110111 01100001 01111001 00101110 00100000 01000100 01101111 01101110 00100111 01110100 00100000 01110100 01100001 01110101 01101110 01110100 00100000 01101101 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 01110010 00100000 01100100 01100101 01101101 01100001 01101110 01100100 01110011 00101110"""
    elif command.find(COMMAND3) >= 0:
        response = "Well, I don't like you either!"
    elif command.find(COMMAND4) >= 0:
        response = "'Ello!'"
    elif command.find(COMMAND5) >= 0:
        response="""
        Hacking user @noobish_security...%%%%done.%%

        downloading fs...%%
        '/home' -- DONE%%
        '/bin' -- DONE%%
        '/usr' -- DONE%%%%%%
        '/etc' -- DONE%%%%
        '/boot' -- DONE %%

        searching for passwords...%%DONE
        this idiot does not have /etc/shadow...
        running 'john /etc/passwd'...%%%%%%%%%%DONE
        root password is 'password123' :%% wow, this guy is so dumb. %%
        running 'cat rootpass.txt | su -'
        waiting...%%%%DONE
        running script...
        [*] Installing kernel-mode rootkit...%%%%%%DONE
        [*] Regenerating intrd-2.64.img%%%%
        [*] Creating hacked initramfs%%
        [*] All done. Have a nice day, you hacked fool. :)"""
    elif "leaderboard" in command:
        # Custom commandhandler for sirexa
        
        leaderboard_command = command.split()
        leaderboard_command = leaderboard_command[1:]
        
        if leaderboard_command[0] == "help":
            response = """sirexa leaderboard v0.0.1
                give point: `@sirexa leaderboard +username`
                example: `@sirexa leaderboard +sirtomato`
                
                take point: `@sirexa leaderboard -username`
                example: `@sirexa leaderboard -notsirtomato`
                
                leaderboard: `@sirexa leaderboard points`"""
        #etc
        
    return response
