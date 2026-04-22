label secret_ending:
    hide bg lobby
    show bg_generic
    "{i}Drip Drip{/i}"
    "You can hear something..."
    "{i}Drip drip{i}"
    "What is that...?"
    mc "Hey, Arce, can you hear that?"
    show arce normal at truecenter
    arce "What?"
    arce "Oh, sorry, can you hear my MP9 all the way through there?"
    show arce sad
    extend "I swear this supergalactic noise-cancelling earphones are useless, dude."
    "You can see his earphones turned backwards, the little speaker pointing outside his supergalactic ears."
    mc "Not that."
    show arce normal
    "{i}Drip Drip{/i}"
    mc "See? There it is again!"
    "{i}Drip Drip{/i}"
    arce "Oh, you mean that {i}Plop{/i} thing?"
    mc "It actually is {i}Drip{/i}, but yeah."
    arce "You scared me for a second, [mcName], that's just the tap."
    mc "..."
    arce "Yeah, just a normal water tap. Not a supergalactic tap..."
    show arce sad
    extend " Way too expensive."
    arce "..."
    show arce normal
    arce "Don't look at me like that, what's wrong?"
    mc "Ain't we supposed to take care of the environment and stuff?"
    extend " Love the nature."
    extend " Love the spring?"
    arce "Yeah, that's why we're taking care of the Zababuglovers mess!"
    mc "And who takes care of OUR mess?"
    arce "Uhhhhh..."
    arce "The Zababuglovers?"
    arce "Oh my blob!"
    show arce sad
    arce "Have we come full circle?"
    extend " We were always the bad guys and the Zababuglovers have always had to take care of our mess without even noticing?"
    arce "My mind is going to explode, [mcName], and you don't want to see that!"
    "He took it a bit too far"
    mc "Not exactly..."
    show arce normal
    mc "I mean, we've seen spriggos dumping their trash on the street."
    mc "We need a lot of gas to travel through space."
    extend "And we're always going from one planet to another!"
    mc "And we even drop our supergalactic car batteries into the ocean."
    arce "...Really?"
    show arce happy
    arce "That sounds fun!"
    mc "It's not!"
    mc "No wonder why all the planet we get to never look like real spring!"
    show arce sad
    arce "Oh my blob, how dare you?"
    show arce normal
    extend "You're actually right, tho."
    arce "Have you look at other planets with real spring?"
    show arce sad
    arce "They don't look like this, [mcName]. I've seen them on the internet."
    arce "..."
    "{i}Drip Drip{/i}"
    show arce normal
    arce "Ok, now this is getting annoying."
    hide arce
    show tap
    "You and Arce fixed the tap."
    "You could see a couple dozens of bucket filled with water."
    hide tap
    "This whole time, blaming the Zababuglovers was not enough."
    "And dropping car batteries in the ocean is not as fun as it looks."
    "..."
    "The next day, you contacted HQ to let them know about your new discovery."
    "At first, they called you crazy."
    "But Arce managed to convince them."
    arce "If we let the tap drip, it'll swamp out of the sink."
    extend " And we spriggos cannot swim!"
    "HQ wasn't happy with this."
    "Not the thing about not knowing how to swim, actually Arce is one of the few spriggos who cannot swim."
    "But the fact that they were going to lose a lot of supergalactic money."
    "Once they let the spriggos know they can actually be wrong and blaming the Zababuglovers wasn't enough..."
    extend "Something changed."
    show arce normal at truecenter
    arce "Lol, this is corny."
    hide arce
    play music minigame
    "For the first time on centuries, true spring will come."
    "And all thanks to a young spriggo."

    "True spring is here..."
    "And so, the legend was born."
    "The cleaner."
    "The destroyer of garbage."
    "The terror of pollution."
    "The god of not throwing car batteries at the ocean."
    "And the name is..."
    show arce happy at truecenter
    "ARCE!"
    hide arce
    "But his companion was important too!"
    if mcSymbol == "heart":
        show symbol heart
        arce "Heh, truly a lovely heart."
    elif mcSymbol == "circle":
        show symbol circle
        arce "That's boring, dude."
    else:
        show symbol star
        arce "The star is my symbol too!"
    "[mcName] can be proud,"
    extend " [mcPronoun] symbol will guide the spriggos next generation."
    hide symbol
    show bg true_spring
    "And finally, the spriggos did it. True spring will be forever on this planet, and soon, in all of the galaxy!"
    "Which, let's be honest, is kinda scary."
    "But it sure looks cool!"



    