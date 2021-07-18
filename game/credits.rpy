# Credits.rpy

# This controls the ending of DDLC and your mod!

# Use this as a starting point if want to override this with your own.

# Import the datetime python library to calculate time.
init python:
    import datetime

# Team Salvato Logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# Style fonts for the credits
style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)

transform credits_scroll:
    subpixel True
    xalign 0.5
    yoffset 740
    linear 15 yoffset -380

# Start of the actual credits scene
label credits:
    stop music fadeout 1.0
    # Reloads DDLC to credits
    $ persistent.autoload = "credits"
    $ renpy.save_persistent()
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    play music "mod_assets/bgm/moddedcredits.mp3" noloop
    scene black
    show credits_header "Monika Has A Gun":
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
        alpha 0.0
        linear 2.0 alpha 1.0
        pause 5.0
        linear 2.0 alpha 0.0
    pause 7
    jump credits2

# This is where the credit scroll starts
label credits2:
    
    python:
        if not player: player = "The Player"
    
    show credits_header "Mod Concept" as credits_h1 at credits_scroll
    show credits_text "My friend Liam" as credits_t1 at credits_scroll
    with None
    
    pause 10
    
    show credits_header "Mod Design" as credits_h2 at credits_scroll
    show credits_text "MineRobber" as credits_t2 at credits_scroll
    with None
    
    pause 10
    
    show credits_header "Lack Of Artistic Talent" as credits_h3 at credits_scroll
    show credits_text "Also MineRobber" as credits_t3 at credits_scroll
    with None
    
    pause 10
    
    show credits_header "Writing" as credits_h1 at credits_scroll
    show credits_text "Honestly most of it was just Dan's writing\nMineRobber only wrote the ending" as credits_t1 at credits_scroll
    with None
    
    pause 8
    
    show credits_header "Characters, in order of appearance" as credits_h2 at credits_scroll
    show credits_text "[player] - [player]\nSayori - Sayori\nYuri - Yuri\nNatsuki - Natsuki\nMonika - Monika" as credits_t2 at credits_scroll
    with None
    
    pause 12
    
    show credits_header "Special Thanks" as credits_h3 at credits_scroll
    show credits_text "Monika\n[player]" as credits_t3 at credits_scroll
    with None
    
    pause 8
    
    python:
        import datetime
        currentyear = datetime.date.today().year
        # Word of God says they're all 18 so just subtract 18 from currentyear
        birthyear = currentyear-18
    
    show credits_header "In Memoriam" as credits_h1 at credits_scroll
    show credits_text "Sayori, Natsuki, Yuri, and Monika\n[birthyear] - [currentyear]" as credits_t1 at credits_scroll
    with None
    
    pause 10
    
    # Shows the Team Salvato Logo
    show credits_ts
    show credits_text "with apologies to": # lul
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    # Fade to black, Ferris Bueller it, and make the player quit
    label postcredits_loop:
        # Game reloads to the postcredits_loop
        $ persistent.autoload = "postcredits_loop"

        # Disables Main Menu, Quick Menu, Everything
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False

        # Fade to black, show Monika.
        scene black
        show monika 2i at t11
        
        # Ferris Bueller time
        $ m_name = "Monika"
        m "...You're still here?"
        m "..."
        m 4n "...It's over."
        m "Go home."
        m "..."
        m 4o "..."
        m 5b "Go."
        hide monika

        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return
