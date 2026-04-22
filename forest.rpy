init python:
    import random

    forest_pool = [
        ("forest_tree1", 10),
        ("forest_tree2", 10),
        ("forest_tree3", 10),
        ("forest_tree4", 10),
        ("forest_tree5", 3),
        ("forest_tree6", 1)
    ]

    def pick_tree():
        name = [f[0] for f in forest_pool]
        weight = [f[1] for f in forest_pool]
        return random.choices(name, weights = weight, k = 1)[0]

    def gen_pos(tries = 20):
        for _ in range(tries):

            x = random.uniform(0.1, 0.9)
            y = random.uniform(0.5, 0.9)

            valid = True

            for f in forest_data:
                if abs(f["x"] - x) < 0.12 and abs(f["y"] - y) < 0.12:
                    valid = False
                    break

            if valid:
                return (x, y)

        return (0.5, 0.7)

    def add_tree():
        tree = pick_tree()
        x, y = gen_pos()

        forest_data.append({
            "type": tree,
            "x": x,
            "y": y
        })



label forest:

    if not first_forest_win:
        show bg forest_dirty

        arce "Man, this forest looks miserable."
        arce "Is full of dead and chopped trees"
        extend " Why the Zababuglovers need wood for, anyways?"
        arce "Oh."
        extend "Some spriggos say they like to chew on hard wood or something like that."
        arce "Have you ever tasted a tree, [mcName]? It doesn't taste good."
        arce "..."
        arce "Anyway, let's get this place clean and full of life again!"

        jump mash_minigame
    else:
        $ dialog = [
            "I hate Falloms, they always say Fall is the best season on the universe... How? All the trees start to lose their leaves! And let's not even begin with the Winteroos, they are bald and so their trees!",
            "The other day i saw a Zababuglover tryig to climb a tree, he fell off.",
            f"Have you ever tried to hug a tree. {mcName}?",
            "I love trees, they cast cool shadows!",
            "What is your favorite kind of tree? Mine is the one that gets pink on spring, but all our planets have a never ending spring, so it looks cool forever!",
            f"Hey, {mcName}, is it possible to drown in a sea of trees?",
            "Forests can be quite scary at night."
        ]

    $ line = renpy.random.choice(dialog)

    arce "[line]"
    arce "Anyway, take our supergalactic shovel and make some room to plant a tree!"
    show bg shovel


    jump mash_minigame