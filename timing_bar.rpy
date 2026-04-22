screen bar_minigame():

    modal True

    default pos = 0.0
    default direction = 1
    default hits = 0
    default speed = 0.01

    default target_start = 0.4
    default target_end = 0.6

    timer 0.01 repeat True action [
        SetScreenVariable("pos", pos + (speed * direction)),
        If(pos >= 1.0, SetScreenVariable("direction", -1)),
        If(pos <= 0.0, SetScreenVariable("direction", 1)),
]

    key "K_SPACE" action If(
    target_start <= pos <= target_end,
    [
        SetScreenVariable("hits", hits + 1),
        SetScreenVariable("speed", 0.01 + (hits * 0.02)),
        If(hits + 1 >= 3, Return(True))
    ],
    Return(False)
)

    frame:
        align (0.5, 0.5)
        padding (30, 30)

        vbox:
            spacing 20
            align (0.5, 0.5)

            text "Press supergalactic SPACE at the right moment!"

            fixed:
                xmaximum 400
                ymaximum 40

                bar:
                    value pos
                    range 1.0
                    xmaximum 400

                add Solid("#c9dab8"):
                    xpos target_start
                    xanchor 0.0
                    xsize int((target_end - target_start) * 400)
                    ysize 38

                add Solid("#2d535b"):
                    xpos pos
                    xanchor 0.5
                    ypos 0.5
                    yanchor 0.5
                    xsize 6
                    ysize 40

            text "Hits: [hits]/3"

label timing_bar:

    play music minigame

    $ result = renpy.call_screen("bar_minigame")

    if result:
        if first_pond_win == False:
            $ first_pond_win = True
            $ add_fish()
            $ fishes_n += 1
            $ renpy.block_rollback()
            show bg pond_base_clean
            arce "Nice catch!"
            arce "Wow, the water is looking crystal clear now."
            extend "Soon, it'll be filled with precious little fishies."
            $ activities["pond"] = True
        else:
            arce "One more sea creature in the pond!"
            $ fishes_n += 1
            $ add_fish()
    else:
        arce "You couldn't even catch swimming trash..."

    call pond_show from _call_pond_show

