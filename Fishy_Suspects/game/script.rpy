# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sherlobs Holmes")
define pd = Character("Commissioner Shrimp")

# The game starts here.

label start:

    play music "/audio/Rain.wav"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg1
    "It was just like any other evening in the bottom of the sea."
    "Dark, deep, and wet."

    "rrinnggg. riinggg.. rriinnggg."

    s "Hello, Sherlobs Holmes speaking."

    "Ayy lobby!"
    "Head of the Police Department.. I guess work never ends."

    s "What can I do for you, boss?"

    pd "You remember that guy-- uhh what's his name? Gobilious? Gobilio?"

    s "You mean Gobius?"

    pd """
    Yeah! yeah yeah. That guy. 

    He sent somethinng to you earlier today. A letter or somethin'.
    """

    "How formal.."

    pd "Anyway, it's on your desk, says it was important."

    s "Alright, I'll check it out."
    s "Thanks for the heads up."

    pd "No problem! See you around lobby!"

    "The phone call ends."

    menu:
        "Time to clock in..."

        "Enter the police department":
            stop music fadeout 1.0
            jump inside_begin


    return

label inside_begin:
    scene bg2
    """
    Upon entering the office, I spot the mentioned letter on your desk.
    
    Sir Gobious...

    My long time acquaintance...
    """

    menu:
        "What could it be about?"

        "Open the letter":
            jump open_letter

label open_letter:
    scene bg3

    "The letter reads:"
    """
    My dear detective,

    Three years have passed since we last converse. 
    
    I've seen all the news regarding your recent cases, and I understand you don't have the leisure, but it would be such a pleasure to have you join us for the celebration of Gob Corp's 30th anniversary. 
    
    There will be appetizers and drinks suited to your taste.

    I have also purchased the red wine you recommended, and I kept an extra bottle in the cellar just for you. 
    
    It would be such a shame to not catch up after all this time. 
    
    Wouldn't you humor me and come have a drink with this old friend?"
    """

    menu:
        "Accept the invitation?"

        "Yes.":
            jump accept_invitation

        "No, throw it in the trash.":
            jump decline_invitation

label accept_invitation:



label decline_invitation:

    
