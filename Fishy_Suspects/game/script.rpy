# The script of the game goes in this file.

# Enables the text shader engine without applying any typewriter or slow-text effect
define config.default_textshader = "typewriter"
define s = Character("Sherlobster", who_color="C10000")
define c = Character("Comissioner", who_color="C14D00")
define cc = Character("CCs", who_color="3E4DD2")
define g = Character("Gobius", who_color="99B529")
define j = Character("Jell", who_color="#a96dfc")
define pf = Character("Pufferfish", who_color="BF8A11")

define audio.SherlobTheme = "/audio/Sherlob.wav"
define audio.popshrill = "/audio/Shrillypop.wav"
define audio.Explore = "/audio/Explore.wav"
define audio.Jelly = "/audio/JellyFih.wav"
define audio.Club = "/audio/ClubMusic.mp3"
define audio.Guilty = "/audio/Gill-ty.wav"
define audio.Jolly = "/audio/JollyFih.wav"
define audio.Gobby = "/audio/Gobbers.wav"

# character transformations
transform slide_left:
    xalign 0.5
    linear 1.0 xalign 0.0

transform slide_right:
    xalign 0.5
    linear 1.0 xalign 1.0
# The game starts here.

image sherlob = im.FactorScale("sherlob.png", 0.65)
image comissioner = im.FactorScale("comissioner.png", 0.65)
image gobius = im.FactorScale("gobius.png", 0.65)
image jell = im.FactorScale("jell.png", 0.65)
image ccs = im.FactorScale("ccs.png", 0.65)
image pf = im.FactorScale("pufferfish.png", 0.65,)

#There is most definitely a better way to organize these images, but for now... Here it is.
# ==============================================================================
# PAGE 1 IMAGES & THUMBNAILS (2 Buttons)
# ==============================================================================

# Button test_1 (Contains A1, A2, A3)
image A1 = "gui/game_menu.png"
image A2 = Transform("images/characters.png", size=(1920, 1080), fit="contain", yalign=0.5)
image A3 = "images/your_image_a3.png"
image thumb_1 = Transform("A1", size=(384, 216))

# Button test_2 (Contains A4)
image A4 = Transform("images/characters.png", size=(1920, 1080), fit="contain")
image thumb_2 = Transform("A4", size=(384, 216))


# ==============================================================================
# PAGE 2 IMAGES & THUMBNAILS (6 Buttons)
# ==============================================================================

# Button test_3
image B1 = Transform("images/IMG_4860.png", size=(1920, 1080), fit="contain")
image thumb_3 = Transform("B1", size=(384, 216))

# Button test_4
image B2 = Transform("images/IMG_4861.png", size=(1920, 1080), fit="contain")
image thumb_4 = Transform("B2", size=(384, 216))

# Button test_5
image B3 = Transform("images/IMG_4862.png", size=(1920, 1080), fit="contain")
image thumb_5 = Transform("B3", size=(384, 216))

# Button test_6
image B4 = Transform("images/IMG_4863.png", size=(1920, 1080), fit="contain")
image thumb_6 = Transform("B4", size=(384, 216))

# Button test_7
image B5 = Transform("images/IMG_4864.png", size=(1920, 1080), fit="contain")
image thumb_7 = Transform("B5", size=(384, 216))

# Button test_8
image B6 = Transform("images/IMG_4865.png", size=(1920, 1080), fit="contain")
image thumb_8 = Transform("B6", size=(384, 216))


# ==============================================================================
# PAGE 3 IMAGES & THUMBNAILS (9 Buttons)
# ==============================================================================

# Button test_9
image C1 = Transform("images/theoffice.png", size=(1920, 1080), fit="contain")
image thumb_9 = Transform("C1", size=(384, 216))

# Button test_10
image C2 = Transform("images/partystart.png", size=(1920, 1080), fit="contain")
image thumb_10 = Transform("C2", size=(384, 216))

# Button test_11
image C3 = Transform("images/insidetheparty.png", size=(1920, 1080), fit="contain")
image thumb_11 = Transform("C3", size=(384, 216))

# Button test_12
image C4 = Transform("images/orchestra.png", size=(1920, 1080), fit="contain")
image thumb_12 = Transform("C4", size=(384, 216))

# Button test_13
image C5 = Transform("images/table.png", size=(1920, 1080), fit="contain")
image thumb_13 = Transform("C5", size=(384, 216))

# Button test_14
image C6 = Transform("images/hallway.png", size=(1920, 1080), fit="contain")
image thumb_14 = Transform("C6", size=(384, 216))

# Button test_15
image C7 = Transform("images/room.png", size=(1920, 1080), fit="contain")
image thumb_15 = Transform("C7", size=(384, 216))

# Button test_16
image C8 = Transform("images/officemurder.png", size=(1920, 1080), fit="contain")
image thumb_16 = Transform("C8", size=(384, 216))

# Button test_17
image C9 = Transform("images/dead.png", size=(1920, 1080), fit="contain")
image thumb_17 = Transform("C9", size=(384, 216))

label splashscreen:

    $ renpy.movie_cutscene('images/IMG_4846.webm')

    return

label start:

    play music SherlobTheme
    scene black
    centered "The sea is full of mysteries."
    centered "But for Detective Sherlobster Holmes," 

    centered "It's just another case waiting to be solved." 

    scene theoffice
    with dissolve
    centered "SHERLOBSTER HOLMES' OFFICE: SEADON POLICE DEPARTMENT 3:00PM" 
    with dissolve

    show sherlob 
    with dissolve

    """
    Sherlobster Holmes sat in desk with one claw stroking his antenna.
    
    He's surrounded by stacks of papers and photographs. 
    
    Notes are scattered around the desk, alongside three empty cups of coffee.

    He's been up all night connecting dots, piecing evidence together, and analyzing witness testimoies. 

    His claw left his antenna and began tapping against his desk.

    {i}Tap. Tap. Tap. Tap. Tap.{/i}

    Then there was a knock at the door.
    """
    play audio "audio/knock.mp3"

    """

    {i}{shader=jitter:1.0, 1.0}KNOCK. KNOCK. KNOCK.{/shader}{/i}
    """
    s"Come in."

    show sherlob at slide_left
    pause

    show comissioner at right
    with dissolve

    "The door opened, revealing Commisioner Shrimp, the head of the Seadon Police Department."

    c"Good morning, Holmes. I see you've been working overtime again."

    s"Well, Commissioner, cases don't solve themselves." 

    c"""Haha, true enough. 
    
    But, Holmes, I think you could afford to take a break once in a while.
    
    I'm not saying this as your superior, but as your friend.
    """

    "Long before Shrimp became the commissioner, and Holmes became a detective, the two had started at the Seadon Police Department together as rookies."

    "Commissioner Shrimp reached into his coat and pulled out a sealed letter."

    c"Before I forget, some fancy looking mailman came by earlier and delivered this for you."

    "He handed the letter to Sherlobster."

    c"They didn't say who it was from, but I trust that you must've got some fancy acquaintances during your travels."

    "Commissioner Shrimp turned towards the door."

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

    {i}I've also purchased the {color=#f00}red wine{/color} I spoke of, and I kept an extra bottle in my office just for you. It would be such a shame to not catch up after all this time. 

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
    play music Explore
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
    play music Club volume 0.75

    """Sherlobster accepted the invitation.
    
    He has been working overtime for far too long. 
    
    There needs to be a good work-life balance, and this invitation is extactly what Sherlobster needs.

    Welp, since he's planning on going, then he must get ready for the party. 
    
    """
    scene partystart
    with dissolve
    pause

    show sherlob at left
    show ccs at right
    with dissolve
    """
    When Sherlobster arrived at the party, he was greeted at the entrance by Gob Corp's secretary, Secretary CCs.

    He was nicknamed CC because Cookiecutter Shark was too long for Sir Gobius.

    Sherlobster has known CCs since their first meeting three years ago. Although CCs officially served as Sir Gobius' secretary, in practice, he was more of a butler. 

    CCs handled almost everything from greeting guests to making sure Sir Gobius' every need was taken care of.

    """

    cc"Detective Holmes, It's been a while. I'm pleased upon your arrival, and I'm sure Sir Gobius would be delighted as well."

    s"Good to see you too, CCs. Hope your daughter's doing well with her health, I've heard the medicine for her treatment have gone to the testing phase. Hopefully, it'll be out by the end of this year."

    "CCs gave Sherlobster a strange look. It was like a half-smile, almost."

    cc"Yes... I've heard about it. My daughter's been doing well too. The doctor's been saying that she's gotten better recently."

    s"Ah. I see."

    """After a brief exchange, Sherlobster thanked CCs and made his way towards the main hall."""
    
    scene insidetheparty
    show jell at left
    show gobius at right
    with dissolve

    """
    Sherlobster opened the door where the party is held.

    What he saw made him stop in his tracks. 

    Across the crowded room stood Sir Gobius, engaging in a heated argument with his wife, Lady Jell.

    The music stopped, even the musicians wanted to hear the couple's quarrel. 

    Being the furthest from the argument, Sherlobster could only hear the crowd's hushed whisper.
    """

    "SOME GUEST" "...I can't believe he'd do that..."
    "ANOTHER GUEST" "...in front of everyone..."
    "ANOTHER OTHER GUEST " "Poor Lady Jell.."
    "SOMEOTHER GUEST" "...they're both crazy..."

    "The argument grew louder until..." 
    
    #there's a glitch here where character temporarily stops- I'll just remove it
    show jell at left
    play music Jelly
    play audio "/audio/slap.mp3"
    with hpunch

    "SLAP!"
    
    """
    Lady Jell struck Sir Gobius across the face with with her gloved tentacle. 

    Silence filled the room.

    Lady Jell stared at the crowd before storming towards the exit.
    """
    hide jell with dissolve

    """

    Sir Gobius remained where he stood, his expression hard to read.
    """

    hide gobius with dissolve

    """

    With a slow stern gaze, Sir Gobius looked across the room, silencing the remaining whispers. 

    The music resumed, and the guess slowly returned to their conversations, pretending as if nothing had happened. 
    """

    show sherlob with dissolve

    """

    Sherlobster's eyes followed Lady Jell as she disappeared through the doors. Before he could do anything, a familiar voice called out to him. 
    """

    g"Holmes!"

    show sherlob at slide_left
    show gobius at right
    with dissolve


    "Sir Gobius approached him with a smile, though there was still a hint of tension in his face."

    g"You actually came! I must admit, I wasn't certain you'd accept my invitation."

    s"Well, you mentioned that {b}bottle of wine{/b}."

    g"Haha, of course. I knew that would get you here."

    s" Are you alright? I couldn't help but notice that you and-"

    g"Ah, yes... That. Nothing for you to concern yourself with, Holmes. Just a little disagreement between husband and wife."

    "Sherlobster could still see he was forcing a smile."

    g"Besides, tonight is a celebration! I wouldn't want something like this to ruin it."

    "Sir Gobius straighten his suit."

    g"Now, if you'll excuse me, I should probably freshen up. Please, make yourself comfortable, Talk with the other guests, try some of the appetizers, and, of course, have a drink or two. Enjoy yourself tonight."

    s"Of course, don't have to tell me twice."

    g"I'll catch up with you later, Holmes."


    menu:
        "Sherlobster watched him leave. Now that Sherlobster has time to think, what should he do first?"

        "Head towards the appetizer table.":
            jump table
        "Head towards the music.":
            jump music
        "Take a break in the hallway." if tablevisited and musicheard:
            jump hallway

#Conditionals so player visits everything before progressing
default tablevisited = False
default musicheard = False



label table:
    scene table
    show sherlob at left
    with dissolve
    $ tablevisited = True
    play music Explore

    """
    Sherlobster's stomach growled as he headed towards the appetizer table. 

    He marveled at the assortment of entrees and appetizers available. 
        
    It seems there are dishes suited for each and every one of the guest's tastes. 

    Sherlobster's eye darted from dish to dish.
    """

    s"Hmm..."

    show ccs at right
    with dissolve
    
    cc"Need assistance deciding, Detective?"

    s"Oh, I almost didn't see you there CCs. Well, there's so many choices that I don't know where to start."

    cc "Then might I recommend the plankton? It's one of Sir Gobius' favorites."

    s "Plankton, huh? Can't say I've had it prepared quite like this before."

    cc"Yes, the chef has quite a particular way of preparing it. I'm sure you'll enjoy it."

    "Sherlobster helped himself to a small serving of the recommended dish. It was indeed delicious."

    s"This is delicious! I've never tasted plankton like this, please, convey my appreciation to the chef, if you will, CCs."

    cc"Of course, Detective."
    jump tableinvestigation



default partytalk = False
default kidtalk = False

label tableinvestigation:
    menu:
        "Ask about the party." if partytalk == False:
            $ partytalk = True
            
            s"It must've been quite a lot of work to organize something like this, especially for the company's 30th anniversary."
            
            cc"""That's certainly true. The company means a lot to Sir Gobius, it's only fitting that he put the same amount of effort into celebrating its anniversary.

            Even the order of each track the orchestra plays had to be decided beforehand. Sir Gobius wanted to ensure the best atmosphere for his guests."""
            
            s"Sounds like he kept you busy."
            
            cc"He certainly does, but once you get used to it, you learn to keep up with his demands."
            
            s"Has he always been this particular?"
            
            cc"{cps=50}{shader=jitter}That's one way to put it.{/shader}{/cps}{nw}" 
            
            "CCs paused, realizing what he had just said."
            
            cc"""Ah, Ahem. Sir Gobius... He's not {i}particular{/i}, he just has high expectations for things. Even... simple things.
            
            And as his butler, I have to see that his wishes are carried out."""
            
            s"Sounds exhausting."
            
            cc"""I don't mind, it's my job to make sure everything is exactly the way {i}he{/i} wants.
            
            {i}Sigh{/i}, forgive me, Detective. I hope I don't sound like I'm complaining. Sir Gobius is a wonderful master, and I'm lucky to be serving him."""

            jump tableinvestigation
        "Ask about his daugther." if kidtalk == False:
            $ kidtalk = True
            s" I know we spoke briefly earlier, but how's your daughter, CCs?"
            
            "CCs' expression softened at the thought of his daughter, his eyes looked a little sad." 
            
            cc"She's... She's doing great, and her health's getting better. I just wish I had more time to spend with her."

            s"I see, I'm sure Sir Gobius wouldn't mind giving you a day off. You've been by his side for nearly ten years!"

            cc"""Haha, yes I have. But the company's been keep Sir Gobius busy, there's simply no time for a day off.

            Whenever I think I've finished one task, there's always another waiting for me.
            
            """
            
            s"After ten years, you'd think he'd give you a little breathing room."

            cc"{cps=50}{shader=jitter}You'd think so, wouldn't you?{/shader}{/cps}{nw}"

            "CCs quickly cleared his throat and straighten himself."

            cc"But that's simply how Sir Gobius is. He expects everthing to be done his way, and I... I suppose I've gotten used to it."

            s"Still, your daughter probably wishes she could see you more."

            "CCs eye's look downcast."

            cc"She probably did."

            s"{i}(Did?){/i}"

            cc"I promised her I'd ask Sir Gobius for a day off. Well, maybe once things settled down, I'm sure he'll be more open to offering it to me."
            jump tableinvestigation

    cc"Oh, would you look at the time! I've been standing idle for too long. Now, if you'll excuse me, I should make sure our other guests are being properly taken care off."

    s"Of course, thank you CCs."


    menu:
        "Head towards the music." if musicheard == False:
            jump music
        "Take a break in the hallway." if tablevisited and musicheard: 
            jump hallway
    
label music:
    scene orchestra
    play music popshrill
    show sherlob at left
    with dissolve
    $ musicheard = True

    """
    Sherlobster wandered deeper into the ballroom, where the sound of the orchestra could be appriecated best.

    Guests danced and chatted along the music, accompanied by the sound of clinking glasses from those who drunk a little too much to be dancing. 

    Turning around to leave the busy scene, Sherlobster bumped into another guest. He stumbled backward, almost falling, before a large fin caught him and held him steady.
    """
    play audio "/audio/rizz.mp3"


    show pf at right
    with dissolve

    s"Ah, pardon me! I wasn't looking where I was turning."

    pf"Ha! No harm done, good sir."

    "Standing in front of Sherlobster was a rather large pufferfish with a wide grin plastered across his face. He helped Sherlobster regain his balance before giving him a friendly pat on the shoulder."

    pf"You alright there?"

    s"Yes, I- ahem, I'm fine. Thank you."

    pf"Good! Wouldn't want you falling over and ruining that nice suit of yours!"

    "Duke Pufferish lets out a hearty laugh."

    "Sherlobster couldn't help but smile."

    s"{i}(He seems like a fun guy to be around.){/i}"

    s"I don't believe we've met before."

    "Sherlobster extends a claw as greeting."

    s"Sherlobster Holmes."

    "Duke Pufferish took his claw and gave it a firm shake."

    pf"A pleasure to finally meet you! I'm Duke Pufferish. Sir Gobius has spoken highly of you, Detective!"

    s"Oh, did he now?"

    pf"Yes, of course. Every time we meet, he always bring you up and talk about the news clippings you were on! He praises every case you solve like a fanboy!"

    s"It sounds like you two know each other quite well."

    pf"Oh, absolutely! Sir Gobius and I have been business partners for years."

    jump musicinvestigation


default selftalk = False
default relation = False


label musicinvestigation:
    menu:
        "Ask about him." if selftalk ==False:
            $ selftalk = True
            s"So, what kind of business do you own? Just out of curiosity."
            
            pf"Oh, I have my fins in a little bit of everything! My family has been in the trading business for generations. We import and export all sorts of goods from different parts of the sea."

            "Duke Pufferish gave a proud grin."

            pf" My grandfather started it when he first arrived at Seadon, he was the one who built the company from the ground up, then my father expanded it, and now I've taken over."

            "Duke Pufferish's face fell slightly."

            pf"We're quite a large company, but not as large as Gob Corp, of course."

            "Duke Pufferish gave a small laugh and scrached the side of his head with a fin."

            pf"When Gobius first started expanding Gob Corp, he came to me and offered a deal... Well, I couldn't turn it down after that! So, I helped him out with shipping routes and connections."

            s" I see."

            pf"He was able to grow his company exponentially and eventually, Gob Corp grew bigger and bigger and even surpasssed my family's business."

            "Duke pufferish's smiled faded and muttered something under his breath"

            pf"{cps=50}{shader=jitter}..If only he didnt hold that against me.{/shader}{/cps}{nw}"

            s" What did you say?"

            "Duke Pufferish stuttered."

            pf"Ah- nothing! Nothing at all!"

            "He coughed to cover up his stutter."

            pf"I'm just so glad I was able to contribute to Gob Corp's success, this company is certainly something extraordinary, just like it's owner."

            s"How one man managed to achieve that much success. Hah, he must have some sort of secret talent for business."

            pf"Ha.. maybe, but Gobius has always been good at keeping his cards close to his chest."
            jump musicinvestigation
        "Ask about his relationship with Sir Gobius." if relation ==False:
            $ relation = True

            "Duke Pufferish puffed his chest out proudly."

            pf"We've been through quite a lot together, the good and bad."

            s"Business partners, huh. I take it you guys must be close after all these years working together? Reminds me of my colleague and I."

            "Duke Pufferish's grin remained, though it seems to twitch for a second."

            pf"I'd... say so! Gobius and I have a long {i}history{/i} together. He's... certainly a memorable fish."

            "Sherlobster raised a brow at 'memorable'."

            pf"Ha! You know what I mean. The man certainly knows how to get what he wants."

            "Duke Pufferish laughed and gave Sherlobster another friendly pat on the shoulder."

            pf"But that's what make him such a sucessful businessfish, his desire for perfection certainly brought him to the top of the food chain!"

            jump musicinvestigation

    
    s"Well, I won't bother you any longer, Duke Pufferfish."

    pf"Oh no, you did not bother me at all Detective, not at all."


    menu:
        "Head towards the table." if tablevisited == False:
            jump table
        "Take a break in the hallway." if tablevisited and musicheard: 
            jump hallway



label hallway:
    play music Jolly volume 0.75
    scene hallway
    pause
    show sherlob at left
    with dissolve 

    "Sherlobster stepped out the ballroom and into the quiet corridor. Once the door closed behind him, he pressed his back against the wall. Muffled music and chatter can still be heard, but muted enough to give his brain a break."

    s"Rich aristocratic parties are definitely not my thing."

    "He took a slow, dragging breath and closed his eyes for a second. Before Sherlobster can even open his eyes, he heard voices coming from around the corner, farther down the corridor."

    "???" "After everything I've had to put up with, you'd think he'd at least have the decency to be discreet."

    "Another voice responded, though Sherlobster couldn't quite make out the words."

    "???" "I never wanted any of this. You know that."

    "Sherlobster recognized her voice."

    show jell at right
    with dissolve

    j"My family thought it was a wonderful arrangement. Sigh... Of course they did. Whatever connections he had, whatever {i}influence...{/i}"

    "Lady Jell scoffed."

    j"Clearly there's no way this man had any influence- other than the dirt he found while digging around where he shouldn't."

    "A pause, it seems the other person responded."

    j"Clearly, it was all a ruse to claim my family's fortune for his own. Everything..."

    "Lady Jell laughed."

    j"...Being his wife doesn't mean I have to pretend I don't know what he does when I'm not around. He thinks he's clever, but he's just hiding behind my family's crest!"

    "Her breathing was clearly louder, and she wason the verge of tears."

    j"Now everyone knows, and he has put shame on this family, this company, and me. UGH! How can I show myself in public now..."

    "Silence once more as the respondant replies. Then Lady Jell reponded with a lowered tone."

    j"If he plans on doing just that, then I'll find a way to stop this nonsense. My family's honor will not fall due to his hands."

    hide sherlob
    hide jell
    with dissolve
    "Sherlobster heard swooshing from the other end of the hallway. He stepped behind a pillar before Lady Jell could see him."

    "As Lady Jell disappeared, the wooshing faded, but Sherlobster remained where he was for a moment. It seems Lady Jell was talking to someone over the phone."

    show sherlob
    with dissolve
    "It's best to return to the banquent hall before anyone noticed him being gone for too long."

    scene insidetheparty
    pause
    show sherlob at left
    with dissolve
    play music Gobby fadein 1.0
    
    "Sherlobster made his way back into the banquet hall."

    "The crowd had thinned since he had left for some air. Some guest had already said their goodbyes, while others still lingered around the tables, finishing their drinks and conversations."

    "Sherlobster loooked around until he spotted Sir Gobius standing near the drinks table. He seems to have freshen himself up."

    "They locked eyes, and Gobius walked up to him holding two drinks."

    show gobius
    with dissolve

    g"Ah, Detective, there you are! I couldn't find you anywhere."

    "Gobius stumbled towards Sherlobster, clearly drunk, and offered a wine glass towards him."

    g"Care for a drink, my friend?"

    s"I suppose another one won't hurt."

    "Sherlobster accepted the wine."

    g" I hope you've been enjoying yourself tonight."

    s" I have, It's certainly been an interesting evening."

    g"Interesting, ey? I hope that's a good thing."

    "Gobius chuckled."

    "The two began to talk, but the celebration seemed to be ending, and guests began to bid their dues."
    
    "GUEST " "Goodnight, Sir Gobius."

    "ANOTHER GUEST " "Happy anniversary, thank you for having us."
    
    g"Ah, thank you for attending, CCs will see you out."

    s"Well, I suppose I should be heading out as well. Thank you for having me tonight."

    "Sherlobster bowed his head goodbye, but Gobius seem to have something to say."

    g" Wait! The wine, I've forgotten about the wine!"

    s"The wine?"

    g"Yes! The red wine we spoked about, it'd be a shame to not serve it to you after all this time. I have even troubled CCs to getting that wine just for this occasion."

    s"I'm afraid I must decline, it's far too late, and I must head back to the office."

    g"Ah... I... I understand. You're busy with your cases."

    "Sir Gobius looks down. It seems he was looking foward to sharing another drink with the detective."

    menu:
        "Stay for the wine.":
            jump mudertime
        "Leave.":
            jump endparty

label mudertime:
    s"It is getting rather late, and I did have more than a couple to drink..."
    
    g"Nonsense! You shouldn't be driving in a state like this. There's a guest room right next door to my office. We don't have to bother anyone else if that's what you're fearing, Detective!"

    s"I-"

    g"Don't worry, my dear friend. The wine is kepted in my office, no one will be disturbed."

    "Before Sherlobster could object, Sir Gobius led him to his office. "

    scene officemurder
    with dissolve 
    pause
    show sherlob at left
    show gobius at right
    with dissolve
    play music Explore fadein 1.0

    "Sir Gobius was overjoyed to say the least. He ushered Sherlobster towards the sofa before hurrying over to his liquor cabinet. "

    "Sherlobster looked around the room."

    "His office was extravagant. Famous painting lined against each wall, while Sir Gobius' desk looked to be custom made with intricate detailed carved into the frame. Even the floor was covered by an expensive carpet that stretched across most of the room.  "

    s"Your office is quite lavish."

    g"Yes, I'm glad you noticed! I spent hours with the contractor making sure it had that effect."

    "Gobius retrieved a bottle from the cabinet and placed it on the table along with two wine glasses. He then sat across from sherlobster on the opposite sofa. "

    g"This is the one, the very bottle I told you about. It has a wonderfully smooth flavor, with a delicate, rich, lingering sweet finish. I think you'll find it absolutely delightful, I'm sure of it."

    "Sherlobster examined the bottle as Sir Gobius poured them each a glass. "

    "Gobius handed him the glass, and they both took a sip of the wine."

    "It was just as Sir Gobius described. The wine was delightfully smooth and rich, with a subtle sweet taste that lingered on the tongue. It was unlike any wine Sherlobster has ever tasted. "

    s"You weren't wrong, this wine is delightful!"

    "They continued their conversation from before, but as the night continued,  it was evident that Sherlobster's exhaustion began to catch up with him."

    "Eventually, Sir Gobius took Sherlobster to the guest room."

    scene room
    with dissolve 
    pause
    show gobius at right
    show sherlob at left
    with dissolve

    g"Get some rest, Detective. I'm sure you'll feel much better in the morning."

    s"Thank you, Sir Gobius. Goodnight."

    hide gobius
    with dissolve

    "Sherlobster settled into bed, barely keeping his eyes open."

    "Just as he was about to fall asleep, a piercing scream was heard."

    "???" "{shader=jitter}AHHHHHHHHHHHHHHHHH{/shader}"
    
    show sherlob at left
    with hpunch
    play music Jelly

    "Sherlobster's eyes shot open."

    hide sherlob
    show sherlob 
    with dissolve
    "He jumps out of bed and rushed towards the sound."
    

    scene hallway
    with dissolve
    pause
    show sherlob at left
    with dissolve

    "The scream had come from Sir Gobius' office. "

    show ccs at right
    with dissolve

    "Secretary CCs was standing inside the office, right by the door. He looked faint, his face pale with fear and horror."

    s"CCs? What happen? What's wrong-"

    "CCs could barely speak, he looked shocked to see the detective."

    "Sherlobster took a look inside."

    "His eyes widened."

    play music Guilty
    scene dead 
    with dissolve
    pause

    "Sir Gobius was lying motionless on the couch, bleeding heavily. Sherlobster rushed to Sir Gobius' side and assessed the situtation immmediately. "

    "There was no use."

    "Sir Gobius was dead."

    scene black 
    with dissolve
    pause
    centered "THE END of CHAPTER 1"
    centered "MORE TO COME"

    return


label endparty:
    g"Goodnight then, I'll send the wine to your office, Sherlobster. A thank you gift for attending, I suppose."

    s"Goodnight, Sir Gobius. I wish for your good health, and your company's continue success."

    "Sherlobster leaves for the night and drives back to the office. "

    "But it seems Sherlobster forgot something crucial:"

    scene black 
    with dissolve
    pause
    play music SherlobTheme

    centered "Driving."
    centered "Under."
    centered "Influence. "

    centered "ENDING: DUI (wait aren't you a cop?)"
    return














