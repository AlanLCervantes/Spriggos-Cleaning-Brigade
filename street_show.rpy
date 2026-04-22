default street_items = {
    "streets_gamereward1": 0,
    "streets_gamereward2": 0,
    "streets_gamereward3": 0,
    "streets_gamereward4": 0
}
init python:

    def pick_street_item():
        return renpy.random.choice(list(store.street_items.keys()))

    def give_street_reward():
        item = pick_street_item()
        store.street_items[item] += 1
        store.last_street_item = item

screen street_reward():

    modal True

    add "Streets/[last_street_item].png":
        align (0.5, 0.5)

    text "You found something!":
        align (0.5, 0.8)

    key "dismiss" action Return()

label street_show:

    $ first_day_passed = True

    call screen street_reward

    hide screen catch_game

    $ activities["streets"] = True
    if all_done():
        "You completed all activities! A new day begins."
        $ reset_activities()
        jump lobby
    else:
        "Back to the lobby..."
        jump lobby

    jump lobby
