# The script of the game goes in this file.

# Enables the text shader engine without applying any typewriter or slow-text effect
define config.default_textshader = "typewriter"
define s = Character("Sherlobster", who_color="C10000")
define c = Character("Comissioner", who_color="C14D00")
define cc = Character("CCs", who_color="3E4DD2")
define g = Character("Gobius", who_color="99B529")
define j = Character("Jell", who_color="")
define pf = Character("Pufferfish", who_color="BF8A11")

define audio.SherlobTheme = "/audio/Sherlob.wav"
define audio.popshrill = "/audio/Shrillypop.wav"
define audio.Explore = "/audio/Explore.wav"
define audio.Jelly = "/audio/JellyFih.wav"
define audio.Club = "/audio/ClubMusic.mp3"

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
    When Sherlobster arrived at the party, he was greeted by the entrance by Gob Corp's secretary, Secretary CCs.

    Sherlobs have known CCs since their meeting three years ago. Although CCs officially served as Sir Gobius' secretary, in practice, he was more of a bulter. 

    CCs handled almost everything from greeting guests to making sure Sir Gobius' every need was taken care of

    """

    cc"Detective Holmes, It's been a while. I'm pleased to see you could make it, and I'm sure Sir Gobius would be delighted as well."

    s"Good to see you too, CCs. Hope your daughter's doing well with her health, I've heard the medicine for her treatment have gone to the testing phase. Hopefully it'll be out by the end of this year."

    "CCs gave Sherlobster a strange look. It was like a half-smile almost."

    cc"Yes, I've heard about it. My daughter's been doing well too. The doctor's been saying that she's gotten better recently."

    s"Ah. I see."

    """After a brief exchange, Sherlob thanked CCs and made his way towards the main hall."""
    
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

    "GUEST1" "...I can't believe he'd do that..."
    "ANOTHER GUEST" "...in front of everyone..."
    "GUEST" "Poor Lady Jell.."
    "SOMEOTHER GUEST" "...they're both crazy..."

    "The argument grew louder until." 
    
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

    With a slow stern gaze, SIr Gobius looked across the room, silencing the remaining whispers. 

    The music resumed, and the guest slowly returned to their conversations, pretending as if nothing had happened. 
    """

    show sherlob with dissolve

    """

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
    play music Explore

    """
    Sherlob stomach growled as he head towards the appetizer table. 

    He marveled at the assortment of entrees and appetizers available. 
        
    It seems there are dishes suited for each and every one of the guest's tastes. 

    Sherlobster's eye darted from dish to dish.
    """

    s"Hmm..."

    show ccs at right
    with dissolve
    
    cc"Need assistance deciding, Detective?"

    s"Oh, I almost didn't see you there CCs. Well, there's so many choices that I don't know how to start."

    cc "Then might i recommend the plankton? It's one of Sir Gobius' favorites."

    s "Plankton, huh? Can't say I've had it prepared quite like this before."

    cc"Yes, the chef has quite a particular way of preparing it. I'm sure you'll enjoy it."

    "Sherlobster helped himself to a small serving of the recommended dish. It was indeed delicious."

    s"This is delicious! I've never tasted plankton like this, please, convey my apprication to the chef, if you will, CCs."

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

            Even the order of each track the orchestra plays had to be decided beforehand. Sir Gobius wanted to ensue the best atmosphere for his guests."""
            
            s"Sounds like he kept you busy."
            
            cc"He certainly does, but once you get used to it, you learn to keep up with his demands."
            
            s"He's always been this particular?"
            
            cc"{cps=100}{shader=jitter}That's one way to put it.{/shader}{/cps}{nw}" 
            
            "CCs paused, realizing what he had just said."
            
            cc"""Ah, Ahem. Sir Gobius... He's not particular, he just have high expectations for things. Even simple things.
            
            And as his bulter, I have to see that his wishes are carried out."""
            
            s"Sounds Exhausting."
            
            cc"""I don't mind, it's my job to make sure everything is exactly the way {i}he{/i} wants.
            
            {i}Sigh{/i}, forgive me, Detective. I hope I don't sound like I'm complaining. Sir Gobius is a wonder master, and I'm lucky to be serving him."""

            jump tableinvestigation
        "Ask about his daugther." if kidtalk == False:
            $ kidtalk = True
            s" I know we spoke briefly earlier, but how's your daughter, CCs?"
            
            "CCs' expression softened at the thought of his daughter, his eyes looked a little sad." 
            
            cc"She's doing great, and her health's getting better. I just wish I had more time to spend with her."

            s"I see, I'm sure Sir Gobius wouldn't mind giving you a day off. You've been by his side for nearly ten years!"

            cc"""Haha, yes I have. But the company's been keep Sir Gobius busy, there's simply no time for a day off.

            Whenever I think I've finsihed one task, there's always another waiting for me.
            
            """
            
            s"After ten years, you'd think he'd give you a little breathing room."

            cc"{cps=100}{shader=jitter}You'd think so, wouldn't you?{/shader}{/cps}{nw}"

            "CCs quickly cleared his throat and straighten himself."

            c" But that's simply how Sir Gobius is. He expects everthing to be done his way, and I... I suppose I've gotten used to it."

            s"Still, your daughter probably wishes she could see you more."

            "CCs eye's look downcast."

            cc"She probably did."

            s"{i}Did?{/i}"

            cc"I promised her I'd ask Sir Gobius for a day off. Well, maybe once things settled down, I'm sure he'll be more open to offering it to me."
            jump tableinvestigation

    cc"Oh, would you look at the time! I've been standing idle for too long. Now, if you'll excuse me, I should make sure our other guests are being properly taken care off"

    s" Of course."


    menu:
        "Head toward the music." if musicheard == False:
            jump music
        "Take a break in the hallway" if tablevisited and musicheard: 
            jump hallway
    
label music:
    scene orchestra
    play music popshrill
    show sherlob at left
    with dissolve
    $ musicheard = True

    """
    Sherlobster wandered deeper into the ballroom, where the sound of the orchestra could be appriecated best.

    Guest danced and chatted along the music, accompanied by the sound of clinking glasses from those who drunk a little too much to be dancing. 

    Turning around to leave the busy scene, Sherlobster bumped into another guest. He stumbled backward, almost falling, before a large fin caught him and held him steady.
    """
    play audio "/audio/rizz.mp3"


    show pf at right
    with dissolve

    s"Ah, pardon me! I wasn't looking where I was turning."

    pf"Ha! No harm done, good sir."

    "Standing in front of Sherlobster was a rather large pufferfish with a wide grin across his face. He helped Sherlobster regain his balance before giving him a friendly pat on the shoulder."

    pf"You alright there?"

    s"Yes, I- ahem, I'm fine. Thank you."

    pf"Good! Wouldn't want you falling over and ruining that nice suit of yours!"

    "Duke Pufferish lets out a hearty laugh."

    "Sherlobster couldn't help but smile."

    s"{i}He seems like a fun guy to be around.{/i}"

    s"I don't believe we've met before."

    "Sherlobster extends a claw as greeting."

    s"Sherlobster Holmes"

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
        "Ask about himself" if selftalk ==False:
            $ selftalk = True
            s"So, what kind of business do you own? Just out of curiosity."
            
            pf"Oh, I have my fins in a little bit of everything! My family has been in the trading business for generations. We import and export all sorts of goods from different parts of the sea."

            "Duke Pufferish gave a proud grin."

            pf" My grandfather started it when he first arrived at Seadon, he was the one who built the company from the ground up, then my father expanded it, and now I've taken over."

            "Duke Pufferish's face fell slightly."

            pf"We're quite a large company, but not as large as Gob Corp, of course."

            "Duke Pufferish gave a small laugh and scrached the side of his head with a fin."

            pf" When Gobius first started expanding Gob Corp, he came to me and offered a deal... Well, I couldn't turn it down after that! So, I helped him out with shipping routes and connections."

            s" I see."

            pf"He was able to grow his company exponentially and eventually Gob Corp grew bigger and bigger and even surpasssed my family's business."

            "Duke pufferish's smiled faded and muttered something under his breath"

            pf"{cps=100}{shader=jitter}..If only he didnt hold that against me.{/shader}{/cps}{nw}"

            s" What did you say?"

            "Duke Pufferish stuttered."

            pf"Ah- nothing! Nothing at all!"

            "He coughed to cover up his stutter."

            pf"Im just so glad I was able to contribute to Gob Corp's success, this company is certainly something extraordinary, just like it's owner."

            s"How one man managed to achieve that much success... He must have some sort of secret talent for business."

            pf"Ha.. maybe, but Gobius has always been good at keeping his cards close to his chest"
            jump musicinvestigation
        "Ask about his relationship with Sir Gobius." if relation ==False:
            $ relation = True
            jump musicinvestigation

            "Duke Pufferish puffed his chest out proudly."

            pf"We've been through quite a lot together. The good and bad moments."

            s"Business partners, huh. I take it you guys must be close after all these years working together? Reminds me of my colleague and I."

            "Duke Pufferish's grin remained, though it seems to twitch for a second."

            pf"I'd say so! Gobius and I have a long {i}history{/i} together. He's... certainly a memorable fish."

            "Sherlobster raised a brow at 'memorable'."

            pf"Ha! You know what I mean. The main certainly knows how to get what he wants."

            "Duke Pufferish laughed and gave Sherlobster another friendly pat on the shoulder."

            pf"But that's what make him such a sucessful businessfish, his desire for perfection certainly brought him to the top of the food chain!"

            jump musicinvestigation

    
    s"Well, I wont bother you any longer, Duke Pufferish."

    pf"Oh no, you did not bother me at all Detective, not at all."


    menu:
        "Head toward the table." if tablevisited == False:
            jump table
        "Take a break in the hallway" if tablevisited and musicheard: 
            jump hallway


label hallway:
    scene hallway
    show sherlob at left
    with dissolve 

    "Sherlobster stepped out the ballroom and into the quiet corridor. Once the door closes behind him, he pressed his back against the wall. Muffled music and chatter can still be heard but muted enough to give him brain a break."

    s"Rich arostrocrate parties are definitely not my thing."

    "He took a slow, dragging breath and closed his eyes to for a break. Before Sherlobster can even open his eyes, he heard voices coming from around the corner, farther down the corridor."

    "???": "After everything I've had to put up with, you'd think he'd at least have the decency to be discreet."

    "Another voice responded, though Sherlobster couldn't quite make out the words."

    "???": "I never wanted any of this. You know that."

    "Sherlobster recognized her voice."

    show ladyjell at right
    with dissolve

    j"My family thought it was a wonderful arrangement. Sigh... Of course they did. Whatever connections he had, whatever {i}influence{/i}..."

    "Lady Jell scoffed."

    j"clearly there's no way this man had any influence other than the dirt he found while digging around where he shouldnt."

    "A pause, it seems the other person responded."

    j"clearly, it was all a ruse to claim my family's fortune for his own. Everything..."

    "Lady jell laughed."

    j"...Being his wife doesn't mean I have to pretend I don't know what he does when I'm not around. He thinks he's clever, but he's just hiding behind my family's crest!"

    "Her breathing was clearly louder and she was clearly on the verge of tears."

    j" Now everyone knows, and he has put shame on me, this family, UGH! How can I show myself in public now..."

    "Silence once more as the respondant replies. then lady jell's reponded with a lowered tone."

    j" If he plans on doing just that, then I'll find a way to stop this nonsense. My family's honor will not fall due to his hands."

    hide sherlob
    hide ladyjell
    with dissolve
    "Sherlobster heard footsteps approaching from the other end of the hallwasy. He stepped behind a pillar before Lady Jell could see him."

    "Her footsteps faded, but Sherlobster remained where he was for a moment. It seems Lady Jell was talking to someone over the phone."

    "It's best to return to the banquent hall before anyone noticed him being gone for too long."

    "Sherlobster made his way back into the banquet hall."

    "The crowd had thinned since he had left for some air. Some guest had already said their goodbyes, while others still lingered around the tables, finsihing their drinks and conversations."

    "Sherlobster loooked around until he spotted Sir Gobius standing neawr the drinks table. He seems to have freshen himself up."

    "They locked eyes and Gobius walked up to him holding two drinks."

GOBIUS: "Ah, Detective, there you are! I couldn't find you anywhere."

Gobius stumbled towards Sherlobster, clearly drunk, and offered a wine glass towards him.

GOBIUS: "Care for a drink, my friend?"

SHERLOBSTER: "I suppose another one won't hurt."

Sherlobster accepted the wine.

GOBIUS:" I hope you've been enjoying yourself tonight."

SHERLOBSTER:" I have, It's certainly been an interesting evening."

GOBIUS:"Interesting, ey? I hope that's a good thing"

Gobius chuckled.

The two begin to talk, but the celebration seem to be ending, and guest begin to bid their dues.

GUEST: "Goodnight, Sir Gobius."
ANOTHERGUEST: "Happy anniversary, thank you for having us."

GOBIUS: "ah, thank you for attending, CCs will see you out."

SHERLOBSTER: "Well, I suppose I should be heading out as well. Thank you for having me tonight."

Sherlobster bowed his head goodbye, but gobius seem to have something to say.

GOBIUS:" Wait! The wine, I've forgotten about the wine!"

SHERLOBSTER: "The wine?"

GOBIUS: "Yes! The red wine we spoked about, it'd be a shame to not serve it to you after all this time. I have even troubled CCs to getting that wine just for this occasion."

SHERLOBSTER: "I'm afraid I must decline, it's far too late, and I must head back to the office."

GOBIUS: "ah... I... I understand. You're busy with your cases."

Gobius seems down, it seems he was looking foward to sharing another drink with the detective. 













