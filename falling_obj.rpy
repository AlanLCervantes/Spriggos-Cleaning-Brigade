init python:
    import random

    streets_pool = [
        ("streets_gametrash1", 10),
        ("streets_gametrash2", 10),
        ("streets_gametrash3", 10),
        ("streets_gametrash4", 10),
        ("streets_gametrash5", 2) 
    ]

    def pick_trash():
        names = [f[0] for f in streets_pool]
        weights = [f[1] for f in streets_pool]
        return random.choices(names, weights = weights, k=1)[0]

    def spawn_object():
        if len(falling_objects) < 10:
            falling_objects.append({
                "x": random.uniform(0.1, 0.9),
                "y": 0.0,
                "speed": random.uniform(0.003, 0.01),
                "type": pick_trash()
            })

    def update_objects():
        to_remove = []

        mx = renpy.get_mouse_pos()[0] / config.screen_width

        for obj in falling_objects:
            obj["y"] += obj["speed"]

            if abs(obj["x"] - mx) < 0.08 and abs(obj["y"] - 0.8) < 0.08:

                if obj["type"] == "streets_gametrash5":
                    store.caught += 3
                else:
                    store.caught += 1

                to_remove.append(obj)

            elif obj["y"] > 1.0:
                store.missed += 1
                to_remove.append(obj)

        for obj in to_remove:
            falling_objects.remove(obj)

        if not store.game_over:
            if store.caught >= 10:
                store.game_over = True
                renpy.jump("catch_win")
            elif store.missed >= 3:
                store.game_over = True
                renpy.jump("catch_lose")


screen catch_game():

    modal True

    if not game_over:
        timer 0.8 repeat True action Function(spawn_object)
        timer 0.01 repeat True action Function(update_objects)
    else:
        timer 0.1 action Return()


    add "Streets/streets_basket.png":
        xpos renpy.get_mouse_pos()[0]
        ypos int(config.screen_height * 0.5)
        anchor (0.5, 0.5)

    for obj in falling_objects:
        add "images/Streets/" + obj["type"] + ".png":
            xalign obj["x"]
            yalign obj["y"]

label catch_win:
    $ first_streets_win = True

    hide screen catch_game

    $ give_street_reward()
    $ renpy.block_rollback()

    jump street_show


label catch_lose:

    hide screen catch_game

    "The whople street is full of trash now..."

    return


label catch_minigame:

    play music minigame

    $ falling_objects = []
    $ caught = 0
    $ missed = 0
    $ game_over = False

    show screen catch_game

    while not game_over:
        $ ui.interact()

    hide screen catch_game

    return