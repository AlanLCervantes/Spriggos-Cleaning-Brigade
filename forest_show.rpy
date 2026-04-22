screen trees_planted():
    zorder 10

    for f in forest_data:
        add "Forest/%s.png" % f["type"]:
            xalign f["x"]
            yalign f["y"]

    key "dismiss" action Return()
    
label forest_show:
    $ first_day_passed = True
    show bg forest_bg
    
    if trees_n == 0:
        arce "Man, they're going ot put us in front of the supergalactic firing squad..."
    elif trees_n >= 1 and flowers_n <= 7:
        #$ renpy.notify(str(flowers_data))
        arce "[mcName], i think we're actually doing a good job. With these trees, this planet will have an eternal spring!"
    elif trees_n >= 8:
        arce "The forest is looking good, [mcName]!"
        extend "You have like..."
        arce "..."
        arce "I don't really know how to count, but it's looking lively!"

    call screen trees_planted

    $ activities["forest"] = True
    if all_done():
        "You completed all activities! A new day begins."
        $ reset_activities()
        jump lobby
    else:
        "Back to the lobby..."
        jump lobby

    return
    
    