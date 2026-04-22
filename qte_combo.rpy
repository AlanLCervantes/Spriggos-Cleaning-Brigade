default qte_keys = ["q", "w", "e", "r", "t"]

screen qte_sequence(keys, time_lim):
    modal True
    default time_left = time_lim
    default index = 0

    timer 0.05 repeat True action SetScreenVariable("time_left", max(time_left - 0.05, 0))

    if time_left <= 0:
        timer 0.01 action Return(False)

    if index < len(keys):

        key "q" action If(keys[index] == "q", SetScreenVariable("index", index + 1), Return(False))
        key "w" action If(keys[index] == "w", SetScreenVariable("index", index + 1), Return(False))
        key "e" action If(keys[index] == "e", SetScreenVariable("index", index + 1), Return(False))
        key "r" action If(keys[index] == "r", SetScreenVariable("index", index + 1), Return(False))
        key "t" action If(keys[index] == "t", SetScreenVariable("index", index + 1), Return(False))

    if index >= len(keys):
        timer 0.01 action Return(True)

    frame:
        align (0.5, 0.4)
        padding (30, 40)

        vbox:
            spacing 25
            align (0.5, 0.5)

            text "Complete the sequence!" size 30

            hbox:
                spacing 15
                xalign 0.5

                for i, k in enumerate(keys):

                    if i < index:
                        text "[k.upper()]" size 50 color "#569082"
                    elif i == index:
                        text "[k.upper()]" size 60
                    else:
                        text "[k.upper()]" size 50 color "#888"

            bar:
                value time_left
                range time_lim
                xmaximum 400

label qte_combo:
    play music minigame

    $ img_overlay = "garden_game"
    show bg garden_empty_clean
    if img_overlay:
        show expression img_overlay as overlay_img zorder 5
    $ sequence_length = 5
    $ time_limit = 3.0

    $ keys = [renpy.random.choice(qte_keys) for i in range(sequence_length)]

    $ result = renpy.call_screen("qte_sequence", keys, time_limit)

    hide overlay_img

    if result:
        show bg garden_empty_clean
        $ img_overlay = "garden_game_suc"
        if img_overlay:
            show expression img_overlay as overlay_img zorder 5
        if first_garden_win == False:
            $ first_garden_win = True
            $ flowers_n += 1
            $ add_flower()
            $ renpy.block_rollback()
            "Great, now the garden is clean and our first flower is... flowering. Let's keep up like that!"
        else:
            "One more flower for the garden!"
            $ flowers_n += 1
            $ add_flower()
            $ renpy.block_rollback()
    

    else:
        $ img_overlay = "garden_game_fail"
        if img_overlay:
            show expression img_overlay as overlay_img zorder 5
        show bg garden_empty
        "Oops..."
        extend " Run."

    hide overlay_img
    
    call garden_show from _call_garden_show
