screen mash_game(time_max=1.0):

    modal True

    default value = 0.5 

    timer 0.02 repeat True action SetScreenVariable(
        "value", max(value - 0.01, 0)
    )

    if value <= 0:
        timer 0.01 action Return(False)

    if value >= time_max:
        timer 0.01 action Return(True)

    key "K_z" action SetScreenVariable("value", min(value + 0.05, time_max))
    key "K_x" action SetScreenVariable("value", min(value + 0.05, time_max))

    frame:
        align (0.5, 0.5)
        padding (30, 40)

        vbox:
            spacing 20
            align (0.5, 0.5)

            text "Press Z and X fast!" size 40

            bar:
                value value
                range time_max
                xmaximum 400

label mash_minigame:

    play music minigame

    $ result = renpy.call_screen("mash_game", 1.0)

    if result:
        $ first_forest_win = True
        "You did it!"
        $ trees_n += 1
        $ add_tree()
        $ renpy.block_rollback()
    else:
        "The soil is too hard, it broke our supergalactic shovel..."

    call forest_show from _call_forest_show
    
    return