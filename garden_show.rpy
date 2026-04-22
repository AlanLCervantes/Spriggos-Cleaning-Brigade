screen garden_flowers():
    zorder 10

    for f in flowers_data:
        add "Garden/%s.png" % f["type"]:
            xalign f["x"]
            yalign f["y"]

    key "dismiss" action Return()
    

label garden_show:
    $ first_day_passed = True
    
    if flowers_n == 0:
        arce "Man, they're going ot put us in front of the supergalactic firing squad..."
    elif flowers_n >= 1 and flowers_n <= 7:
        #$ renpy.notify(str(flowers_data))
        arce "[mcName], i think we're actually doing a good job. One more spring creature on this planet!"
    elif flowers_n >= 8:
        arce "The garden is looking good, [mcName]!"
        extend "You have like..."
        arce "..."
        arce "I don't really know how to count, but it's looking lively!"

    call screen garden_flowers

    $ activities["garden"] = True
    if all_done():
        "You completed all activities! A new day begins."
        $ reset_activities()
        jump lobby
    else:
        "Back to the lobby..."
        jump lobby

    return
    