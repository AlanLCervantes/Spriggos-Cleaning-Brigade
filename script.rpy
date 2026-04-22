# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcName]", color="#8d5489")
define arce = Character("Arce", color="#2d535b")

define audio.spriggos1 = "audio/Spriggos1.wav"
define audio.minigame = "audio/minigame.wav"

default mcName = ""
default hasName = False
default mcPronoun = ""
default mcSymbol = ""

default first_day_passed = False

default first_pond_win = False
default fishes_data = []
default fishes_n = 0

default first_garden_win = False
default flowers_data = []
default flowers_n = 0

default first_forest_win = False
default forest_data = []
default trees_n = 0

default first_streets_win = False

label pickaName:
    $ renpy.dynamic('ready', 'uname', 'cdialogue')
    $ ready = False
    $ cdialogue = "Alright, cadet, what's your name?"
    $ uname = renpy.input(cdialogue, exclude='1234567890{}[]()|\/*-=+<>?;:"&^!@#$%~` ').strip().capitalize()
    if uname == "Arce":
        arce "No way, are you my long lost cousin!?"
        arce "No?"
        arce "Stop fooling around then!"
        arce "Oh, is that really your name?"
        arce "Well... more than half our population is called Spriggo Jenkings..."
        $ mcName = uname
        $ ready = True
        $ hasName = True
        arce "Anyway, [mcName]."
        arce "With our help, this planet will be squeaky clean and full of life again."
    elif uname == "":
        arce "Excuse meeee."
        arce "Are you listening?"
        arce "I said..."
        $ hasName = False
    else:
        $ mcName = uname
        $ ready = True
        $ hasName = True
        arce "Ok, [mcName]."
        arce "With your help, this planet will be squeaky clean and full of life again."

    return

label customMC:
    arce "Alright, so [mcName], what are your pronouns?"

    menu:
        "He/Him":
            $ mcPronoun = "his"
        "She/Her":
            $ mcPronoun = "her"
        "They/Them":
            $ mcPronoun = "their"
        "Other":
            $ mcPronoun = renpy.input("Write your pronouns:", exclude='1234567890{}[]()|\/*-=+<>?;:"&^!@#$%~`').strip()
        
    arce "Last thing."
    extend " What symbol do you want to wear on your supergalactic cleaner uniform?"
    menu:
        "Loving heart":
            $ mcSymbol = "heart"
        "Amazing star":
            $ mcSymbol = "star"
        "Boring circle":
            $ mcSymbol = "circle"

    return

label start:
    
    call pickaName from _call_pickaName

    call customMC from _call_customMC

    show bg_generic
    show spaceship
    arce "In a galaxy far, far away fom ours, thousands of planets have died."
    "Zababuglovers have led their ecosystems dry to the core."
    extend " The let all their water go to waste."
    extend " Their soil unable to grow any crop."
    extend " Their seas have no life now."
    hide spaceship
    show arce sad at truecenter
    arce "Zababuglovers are an evil kind, you see."
    arce "Everywhere they go, life dies and goes to waste."
    show arce normal
    arce "So, it's our duty as spriggos to bring back the life to those planets."
    arce "Life will return, flowers will flourish, trees will grow."
    arce "We'll bring spring (Hehe) to every planet the Zababuglovers have killed."
    show arce normal
    arce "Soon, every corner of the galaxy will be filled to the brim with nature!"
    arce "The last known location from the Zababuglovers was at galaxy Glubglobaglepglep "
    show arce sad
    extend "quadrant... Zapzib... gra... baglon..."
    show arce normal
    arce "Yeah, Zapzibgrabaglon."
    show arce happy
    arce "Planet Lele."
    arce "A float of spriggos will be send there."
    arce "But not just any float, no."
    show arce normal
    extend " Only the BEST of the BEST."
    hide arce
    "..."
    "And so, the legend was born."
    "The cleaner."
    "The destroyer of garbage."
    "The terror of pollution."
    "The god of"
    extend " ...well, that's enough."
 
    jump lobby
