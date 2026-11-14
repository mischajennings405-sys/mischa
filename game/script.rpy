# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Claire", color= "#ffcccc")
define a = Character("Andrew", color= "#ffcccc")

# The game starts here.

label start:


    scene bg dimstreet

    show claire annoyed

    # These display lines of dialogue.

    c "We're done."

    show andrew sad

    a "NO CLAIRE! I swear i'll change! I promise!"

label chaseafterher:
    
    

label gohome:



    # This ends the game.


    return
