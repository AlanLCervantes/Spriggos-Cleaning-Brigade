screen fishes_underwater():
    zorder 10

    for f in fishes_data:
        add "Pond/%s.png" % f["type"]:
            xalign f["x"]
            yalign f["y"]

    key "dismiss" action Return()
    
label pond_show:
    show bg underwater
    $ first_day_passed = True

    if fishes_n == 0:
        arce "Man, they're going ot put us in front of the supergalactic firing squad..."
    elif fishes_n >= 1 and fishes_n <= 7:
        #$ renpy.notify(str(flowers_data))
        arce "[mcName], look at them swim!"
    elif fishes_n >= 8:
        arce "The garden is looking good, [mcName]!"
        extend "You have like..."
        arce "..."
        arce "I don't really know how to count, but it's looking lively!"

    call screen fishes_underwater

    $ activities["pond"] = True
    if all_done():
        "You completed all activities! A new day begins."
        $ reset_activities()
        jump lobby
    else:
        "Back to the lobby..."
        jump lobby
    
    $ first_day_passed = True

    return
    
    