init python:
    import random

    pond_pool = [
        ("fish1", 10),
        ("fish2", 10),
        ("fish3", 10),
        ("fish4", 10),
        ("fishspec1", 3),
        ("fishspec2", 1)
    ]

    def pick_fish():
        name = [f[0] for f in pond_pool]
        weight = [f[1] for f in pond_pool]
        return random.choices(name, weights = weight, k = 1)[0]

    def gen_pos(tries = 20):
        for _ in range(tries):

            x = random.uniform(0.1, 0.9)
            y = random.uniform(0.5, 0.9)

            valid = True

            for f in fishes_data:
                if abs(f["x"] - x) < 0.12 and abs(f["y"] - y) < 0.12:
                    valid = False
                    break

            if valid:
                return (x, y)

        return (0.5, 0.7)

    def add_fish():
        fish = pick_fish()
        x, y = gen_pos()

        fishes_data.append({
            "type": fish,
            "x": x,
            "y": y
        })


label pond:

    if not first_pond_win:
        show bg pond_base

        arce "Ugh, it smells so bad here!"
        extend " And here i thought it'd be clean enough to take a swin."
        arce "Water is so polluted a fourth eye would grow on my face!"
        arce "..."
        arce "We better get to cleaning, then."
        arce "Lucky for us, we have our supergalactic cleaning... "
        extend " uhhh."
        show bg net
        arce "This thing!"
        arce "What are you waiting for? Get to cleaning!"

    else:
        show bg pond_base_clean
        $ dialog = [
            "Everyone says swimming is a summer thing, but going to the beach on spring is cheaper!",
            "Those fishes sure look tasty.",
            "No Zababuglovers on the sight... good, i don't wat them to take me for an octopus and eat me!",
            f"I have a funny joke for you, {mcName}. Why did the fish cross the road?",
            "It still smells like fish.",
            f"Hey, {mcName}, what's your favourite fish? Mine is the clown fish, it reminds me of you!",
            f"Hey, {mcName}, i don't want to go fishing for fishies, i just want to let them freely swim!"
        ]

        $ line = renpy.random.choice(dialog)
        arce "[line]"
    
    show bg net
    
    jump timing_bar