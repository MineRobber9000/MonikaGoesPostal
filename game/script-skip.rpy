label skip_to_ch5:
    scene black
    with dissolve
    play music m1
    "Hey, MineRobber here."
    "...Yeah, the original release of this mod was kind of a mess."
    "I forgot to unprivate the GitHub repo, so nobody got to play my shit mod at the time."
    "But now, 365 days later, I've endeavored to fix some things about it."
    "Namely: Don't make the player sit through the entirety of Act 1 to get to the bit."
    "It's just... {w=0.3}not interesting, right?"
    "If you wanted to play Act 1, you could just go play the base game."
    "Anyways, since we're now skipping right to when stuff happens (admittedly cutting down on this mod's length), we need to clarify some things."
    menu:
        "Who did you invite over to your house on Sunday?"
        "Natsuki":
            $ ch4_scene="natsuki"
            "...Insert Chris Hansen joke here."
        "Yuri":
            $ ch4_scene="yuri"
            "...Insert man of culture joke here."
    "Just kidding, just kidding."
    menu:
        "What did you tell Sayori?"
        "I love you.":
            $ sayori_confess=True
        "You'll always be my dearest friend.":
            $ sayori_confess=False
    "Alright! Without further ado, let us get to the point."
    return
