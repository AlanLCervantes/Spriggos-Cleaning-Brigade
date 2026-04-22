default activities = {
    "garden": False,
    "pond": False,
    "forest": False,
    "streets": False,
}

init python:
    def reset_activities():
        for k in activities:
            activities[k] = False

    def all_done():
        return all(activities.values())

    def fix_activities():
        for k in ["garden", "pond", "forest", "streets"]:
            if k not in activities:
                activities[k] = False


label lobby:
    play music spriggos1
    $ fix_activities()
    show bg lobby

    if not first_day_passed:
        arce "Rise and shine, [mcName]. Wake up early so the spring can come as soon as possible."
        arce "It is our duty, as the Spriggos Cleaning Brigade to bring the spring to this planet and all of its creatures!"
        arce "Fishes, flowers, trees..."
        arce "Ahhhh, i can already smell the nature."
        arce "Let's go, [mcName]. Spring is waiting for us!"
        "And so, another day of cleaning began."

    else:
        $ dialog = [
            f"Come on, {mcName}, let's go!",
            "I should have joined the Spriggos Cooking Brigade...",
            f"{mcName}, i don't really feel like cleaning today..."
            f"Hey, {mcName}, i just drank two energy drinks and i think i feel ready to clean the 4th dimension!",
            "Man, we've been in this planet forever... ",
            "If only the Zababuglovers have not eaten all the nature like hundreds of times!",
            f"We've been following the Zababuglovers for years and we haven't achieved to bring the spring in any of the planets we come, what are we doing wrong, {mcName}!?",
            "My grandgrandgrandfather died proud while doing his duty on planet Lala. I wonder if he is watching me from the stars!",
            f"Hey, {mcName} have it told you about the day i got jumped by a group of ninja Zababuglovers? My mind went blank, my body started to get hot, i closed my eyes and when i opened them... all the Zababuglovers were lying on the ground. I'm a savage, you see.",
            "Heh, you're looking funny today.",
            f"{mcName}, it's tuesday.",
            f"We've been here only a couple hundreds of years and i feel like we're making good progress. Don't you think, {mcName}?",

        ]

        "Cleaning is an everyday task."
        "..."
        $ line = renpy.random.choice(dialog)

        arce "[line]"

    menu:
        "Go to the garden" if not activities["garden"]:
            jump garden
        "Go to the garden (Done)" if activities["garden"]:
            "Already done."
            jump lobby

        "Go to the pond" if not activities["pond"]:
            jump pond
        "Go to the pond (Done)" if activities["pond"]:
            "Already done."
            jump lobby

        "Go to the forest" if not activities["forest"]:
            jump forest
        "Go to the forest (Done)" if activities["forest"]:
            "Already done."
            jump lobby

        "Go to the streets" if not activities["streets"]:
            jump streets
        "Go to the streets (Done)" if activities["streets"]:
            "Already done."
            jump lobby

        "This planet is clean enough" if can_normal_end():
            jump normal_ending

        "You can hear something..." if can_secret_end():
            jump secret_ending