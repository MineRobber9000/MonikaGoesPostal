# Script.rpy
# This is the main script that DDLC/Ren'Py calls upon to start
# your mod's story! 

label start:

    # Configures your mod to use a ID to prevent users from cheating.
    # Leave this as default and only change the value 'persistent.anticheat' has
    # in definitions.rpy if you want to change it
    $ anticheat = persistent.anticheat

    # Controls what chapter the game starts for the poem game.
    $ chapter = 0

    # This makes sure if the user quits during pause, 
    # it is set to false after restarting the game. Precaution.
    $ _dismiss_pause = config.developer

    # Names of the Characters
    # To add a character -> $ mi_name = "Mike". Don't forget to
    # add them also in definitions.rpy!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # Controls whether we have a menu in the textbox or not.
    $ quick_menu = True

    # Controls whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited' than 'style.normal'
    $ style.say_dialogue = style.normal

    # Controls whether Sayori is dead. Leave this alone unless needed.
    $ in_sayori_kill = None
    
    # Controls whether we allow skipping dialogue.
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Start of the script
    # '$ chapter = 0' controls the chapter number the game is on for the poem game.
    # 'call tutorial_selection' controls what label to call from in your script files
    # Make sure to change this when coding your mod, else your player will face a script error

    $ chapter = 0
    call ch0_main
    call poem

    # Day 1
    $ chapter = 1
    call ch1_main
    # 'call poemresponse_start' calls the poem response game
    call poemresponse_start
    call ch1_end

    call poem

    $ chapter = 2
    call ch2_main
    call poemresponse_start
    call ch2_end

    call poem

    $ chapter = 3
    call ch3_main
    call poemresponse_start
    call ch3_end

    $ chapter = 4
    call ch4_main

    ## try: renpy.file(config.basedir + "/hxppy thxughts.png") checks if there is a file
    # where DDLC.exe (.app/.sh for MacOS/Linux) called 'hxppy thxughts.png'
    ## except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    # writes 'hxppy thxughts.png' to the main directory if not found.
    python:
        if renpy.android:
            # For Android, the try and excepts must be formatted like so with this but replace
            # hxppy thxughts.png with the file you want to write.
            ## try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
            ## except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
            try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
            except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        else:
            try: renpy.file(config.basedir + "/hxppy thxughts.png")
            except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    $ chapter = 5
    call ch5_main

    #ends the game (not credits)
    call endgame
    jump credits

# the end label of the game. Not the credits.    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

