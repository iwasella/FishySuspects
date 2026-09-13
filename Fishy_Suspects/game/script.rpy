# The script of the game goes in this file.

# Enables the text shader engine without applying any typewriter or slow-text effect
define config.default_textshader = "typewriter"
define s = Character("Sherlobster")
define c = Character("Comissioner")
define cc = Character("CCs")
define g = Character("Gobius")

# character transformations
transform slide_left:
    xalign 0.5
    linear 1.0 xalign 0.0

transform slide_right:
    xalign 0.5
    linear 1.0 xalign 1.0
# The game starts here.

label start:

    play music "/audio/Rain.wav"
    scene black
    show text "The sea is full of mysteries." at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    show text "But for Detective Sherlobster Holmes," at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    show text "It's just another case waiting to be solved." at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    pause 1

    scene police office
    with dissolve
    pause 1
    show text "SHERLOBSTER HOLMES' OFFICE: SEADON POLICE DEPARTMENT 3:00PM" at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    pause 2

    show sherlob 
    with  dissolve

    """
    Sherlobster Holmes sat in desk with one hand stroking his antenna.
    
    He's surrounded by stacks of papers and photographs. 
    
    Notes are scattered around the desk, alongside three empty cups of coffee.

    He's been up all night connecting dots, piecing evidence together, and analyzing witness testimoies. 

    His hand left his antenna and began tapping against his desk.

    {i}Tap. Tap. Tap. Tap. Tap.{/i}

    {i}{shader=jitter:1.0, 1.0}KNOCK. KNOCK. KNOCK{/shader}{/i}
    """
    s"Come in"

    show sherlob at slide_left
    pause

    show comissioner at right
    with dissolve

    "The door opened, revealing Commisioner Shrimp, head of the Seadon Police Department."

    c"Good morning, Holmes. I see you've been working overtime again."

    s"Well, Commissioner, cases don't solve themselves." 

    c"""Haha, true enough. 
    
    But, Holmes, I think you could afford to take a break once in a while.
    
    I'm not saying this as your superior, but as your friend.
    """

    "Long before Shrimp became commissioner, and Holmes became a detective, the two had started at the Seadon Police Department together as rookies."

    "Commissioner Shrimp reached into his coat and pulled out a sealed letter."

    c"Before I forget, some fancy looking mailman came by earlier and delivered this for you."

    "He handed the letter to Sherlobster."

    c"They didn't say who it was from, but I trust that you must've got some fancy acquaintances during your travels."

    "Commissioner Shrimp turned toward the door."

    c"Anyways, I best be on my way. Lunch is calling, and I'm straving. Let me know what that letter says, 'kay?"

    s"Haha, of course. I'll let you in on all the gossip later."

    hide comissioner
    with dissolve
    pause 1
    show sherlob at center
    with dissolve
    "Comissioner Shrimp left the office, closing the door behind him."

    "Sherlobster stared at the envelope before opening it and began to read."

    """
    {i}My dear detective,

    {i}Three years have passed since we last spoke.
    
    {i}I've seen all the news regarding your recent cases, and I understand you don't have the leisure these days. 
    
    {i}Still, it would be such a pleasure to have you join us for the celebration of Gob Corp's 30th anniversary. 
    
    {i}There will be appetizers and drinks suited to your taste.

    {i}I've also purchased the {color=#f00}red wine{/color} you recommended, and I kept an extra bottle in the cellar just for you. It would be such a shame to not catch up after all this time. 

    {i}Wouldn't you humor me and come have a drink with this old friend?

    {i}Yours, {b}Sir P. Gobius{/b}{/i}

    It's a letter from an old acquaintance.
    
    Sir Gobius was a passerby from an old case three years ago.
    
    He remembered Gobius mentioning that he was the owner of a multimillion company.

    Sherlobster stared at the letter.
    """

    s"It would nice to catch up and {shader=wave}have a taste of that wine{/shader}... but what about work?"

    "Could Commissioner Shrimp be right? Maybe he can afford to take a break once in a while."

    menu:
        "Go to the party?"

        "Yes, work can wait.":
            jump partystart
        "No, throw it in the trash.":
            jump trash

label trash:
    scene black
    show text "Sherlobster decided to throw the party invitation in the trash can." at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    show text "What did you expect? A trophy?" at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    show text "ENDING: WORKAHOLIC" at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    pause 1
    return

label partystart:
    """Sherlobster accepted the invitation.
    
    He has been working overtime for far too long. 
    
    There needs to be a good work-life balance, and this invitation is extactly what Sherlobster needs.

    Welp, since he's planning on going, then he must get ready for the party. 
    
    """
    scene birthday
    with dissolve
    pause 1
    show text "GOB CORP 30TH ANNIVERSARY PARTY 6:07PM" at truecenter 
    with dissolve
    pause 2.0
    hide text
    with dissolve
    pause 2

    show sherlob at left
    show CCs at right
    with dissolve
    """
    When Sherlobster arrived at the party, he was greeted by the entrance by Gob Corp's secretary, Secretary CCs.

    Sherlobs have known CCs since their meeting three years ago. Although CCs officially served as Sir Gobius' secretary, in practice, he was more of a bulter. 

    CCs handled almost everything from greeting guests to making sure Sir Gobius' every need was taken care of

    """

    cc"Detective Holmes, It's been a while. I'm pleased to see you could make it, and I'm sure Sir Gobius would be delighted as well."

    s"Good to see you too, CCs. Hope your daughter's doing well with her health, I've heard the medicine for her treatment have gone to the testing phase. Hopefully it'll be out by the end of this year."

    "CCS gave Sherlobster a strange look. It was like a half-smile almost."

    cc"Yes, I've heard about it. My daughter's been doing well too. The doctor's been saying that she's gotten better recently."

    s"Ah. I see."

    """After a brief exchange, Sherlob thanked CCs and made his way towards the main hall."""
    
    scene insideparty
    with dissolve
    pause 1
    #he goes to the center of the screen entering from the right
    show sherlob with moveinright

    """
    Sherlobster opened the door where the party is held.

    What he saw made him stop in his tracks. 

    Across the crowded room stood Sir Gobius, engaging in a heated argument with his wife, Lady Jell.

    The music stopped, even the musicians wanted to hear the couple's quarrel. 

    Being the furthest from the argument, Sherlobster could only hear the crowd's hushed whisper.
    """

    "GUEST1:" "...I can't believe he'd do that..."
    "ANOTHER GUEST:" "...in front of everyone..."
    "GUEST:" "Poor Lady Jell.."
    "SOMEOTHER GUEST:" "...they're both crazy..."

    "The argument grew louder until." 
    
    scene insideparty
    with hpunch
    #there's a glitch here where character temporarily stops- I'll just remove it
    show sherlob
    with dissolve

    "SLAP!"
    
    """
    Lady Jell struck Sir Gobius across the face with with her gloved hand. 

    Silence filled the room.

    Lady Jell stared at the crowd before storming towards the exit.

    Sir Gobius remained where he stood, his expression hard to read.

    With a slow stern gaze, SIr Gobius looked across the room, silencing the remaining whispers. 

    The music resumed, and the guest slowly returned to their conversations, pretending as if nothing had happened. 

    Sherlobster's eyes followed Lady Jell as she disappeared through the doors. Before He can do anything, a familiar voice called out to him. 
    """

    g"Holmes!"

    show sherlob at slide_left
    show gobius at right
    with dissolve


    "Sir Gobius approached him with a smile, though there was still a hint of tension in his face."

    g"I'm so glad you actually came. I must admit, I wasn't certain you'd aaccept my invitation."

    s"Well, you mentioned that {b}bottle of wine{/b}."

    g"Haha, of course. I knew that would get you here."

    s" Are you alright? I couldn't help but notice that you and-"

    g"Ah, yes... That. Nothing for you to concern yourself with, Holmes. Just a little disagreement between husband and wife."

    "Sherlobster can still he was forcing a smile"

    g"Besides, tonight is a celebration! I wouldn't want something like this to ruin it."

    "Sir Gobius straighten his suit."

    g"Now, if you'll excuse me, I should probably freshen up. Please, make yourself comfortable, Talk with the other guests, try some of the appetizers, and, of course, have a drink or two. Enjoy yourself tonight."

    s"Of course, don't have to tell me twice."

    g"I'll catch up with you later, Holmes."


    menu:
        "Sherlobster watched him leave. Now that Sherlobster has time to think, what should he do first?"

        "Head toward the appetizer table.":
            jump table
        "Head toward the music.":
            jump music
        "Take a break in the hallway" if tablevisited and musicheard:
            jump hallway

#Conditionals so player visits everything before progressing
default tablevisited = False
default musicheard = False

label table:
    scene table
    show sherlob at left
    with dissolve
    $ tablevisited = True

    """
    Sherlob stomach growled as he head towards the appetizer table. 

    He marveled at the assortment of entrees and appetizers available. 
        
    It seems there are dishes suited for each and every one of the guest's tastes. 
    """

    show CCs at right
    """
    Confused on where to start, Bulter CCs arrives and recommended a dish of plankton. They converse about the party and their jobs. 
    """

    menu:
        "Head toward the music." if musicheard == False:
            jump music
        "Take a break in the hallway" if tablevisited and musicheard: 
            jump hallway
    
label music:
    scene music
    show sherlob at left
    with dissolve
    $ musicheard = True

    "There's an orchestra playing in the corner."
        
    menu:
        "Head toward the table." if tablevisited == False:
            jump table
        "Take a break in the hallway" if tablevisited and musicheard: 
            jump hallway


label hallway:
    scene hallway
    "we in the halllwayyy"















