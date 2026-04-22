default falling_objects = []
default caught = 0
default missed = 0
default game_over = False
default player_y = 0.85

label streets:
    hide bg lobby
    if first_streets_win == False:
        "Walking through the streets of Planet Lele..."
        arce "Not the best place to catch fresh air."
        "Supergalactic flying cars come buzzing, the air is filled with smog."
        arce "I don't think this is good for the environment, you know?"
        arce "All this heat, [mcName], it doesn't make me feel at spring at all!"
        arce "It feels like summer."
        extend " And who likes summer? Only Summeros like it!"
        show bg streets_air
        "While Arce is busy being loud, you can see a supergalactic flying car... flying around."
        "You point at the sky and Arce stops blabbering."
        show bg streets_air_trash
        arce "Hey, what is that guy doing!?"
        arce "Nooooo!"
        extend "Our own people against us..."
        arce "[mcName], you are my only true allie in this blob forsaken planet, we have to do something!"
        "Arce hands you a not so supergalactic basket."
        extend "More like... a supercommon basket."
        arce "We have to catch all the trash before it gets everything dirty!"
    else:
        show bg streets_air_trash
        arce "Man, this people never learn!"
        arce "Hey, babahead, stop throwing your trash at the street!"
        arce "Come on, [mcName], we can't let it get the street dirty!"
    
    call catch_minigame from _call_catch_minigame
    return