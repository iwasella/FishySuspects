# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sherlobs Holmes")
define pd = Character("Commissioner Shrimp")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    "It was just like any other evening in the bottom of the sea."
    "Dark, deep, and wet."

    "rrinnggg. riinggg.. rriinnggg."

    s "Hello, Sherlobs Holmes speaking."

    "Ayy lobby!"
    "Head of the Police Department.. I guess work never ends."

    s "What can I do for you, boss?"

    pd ""

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
