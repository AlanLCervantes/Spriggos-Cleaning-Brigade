init python:
    import random

    flower_pool = [
        ("flower", 10),
        ("flower1", 10),
        ("flower2", 10),
        ("flower3", 10),
        ("flower4", 10),
        ("flower5", 3),
        ("flowerspec", 1)
    ]

    def pick_flower():
        name = [f[0] for f in flower_pool]
        weight = [f[1] for f in flower_pool]
        return random.choices(name, weights = weight, k = 1)[0]

    def gen_pos(tries = 20):
        for _ in range(tries):

            x = random.uniform(0.1, 0.9)
            y = random.uniform(0.5, 0.9)

            valid = True

            for f in flowers_data:
                if abs(f["x"] - x) < 0.12 and abs(f["y"] - y) < 0.12:
                    valid = False
                    break

            if valid:
                return (x, y)

        return (0.5, 0.7)

    def add_flower():
        flower = pick_flower()
        x, y = gen_pos()

        flowers_data.append({
            "type": flower,
            "x": x,
            "y": y
        })


label garden:

    if not first_garden_win:
        show bg garden_empty

        arce "HOW'S THIS EVEN SUPOSSED TO BE A GARDEN!?"
        extend " Uhhh, what's that black stuff?"
        arce "..."
        arce "Anyway, let's get this thing clean!"

        jump qte_combo
    else:
        $ dialog = [
            "Spring, here we go!",
            "Eating flowers is good for your health! ...I made up that one.",
            "No Zababuglovers on the sight... let's go.",
            "So the other day was at the park and there was this guy who told me... I don't remember what he told me.",
            "Flowers are really cool, you know? Sometimes I can hear their voices... They are often asking me to play with fire inside building and stuff. Funny little creatures!",
            f"Hey, {mcName}, what's your favourite flower? Mine is pogranpagloberips. Lesser beings known then as poppies!",
            f"Hey, {mcName}, how is water made? It comes like, from fishes and stuff?"
        ]

    $ line = renpy.random.choice(dialog)

    arce "[line]"

    jump qte_combo