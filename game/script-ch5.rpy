define config.debug_sound = True

label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    "I stammer, embarrassed."
    "Did Sayori really tell her about it that quickly?"
    if sayori_confess:
        "That we're...a couple now?"
        "I didn't really plan on bringing it up with anyone yet..."
    else:
        "About how I basically turned down her confession?"
        "That makes me really seem like the bad guy here..."
        "But I'm the one who knows what's best for her, right?"
    mc "Jeez..."
    mc "You don't know the full story at all, so..."
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika zorder 1 at thide
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem (poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "What's wrong?"
    mc "Ah, nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Try not to take too long, okay?"
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    scene bg sayori_bedroom with None
    pause 4
    stop music fadeout 1
    "She's still sound asleep."
    "I decide to shake her awake."
    mc "Come on, dummy, it's time for school!"
    show sayori 1ba at t11
    "She slowly blinks herself awake."
    s "...It is?"
    "Then she looks over at her alarm clock, which says the time is 09:12."
    s "...I overslept again!"
    scene bg residential_day with wipeleft
    "Sayori makes eggs and toast for breakfast, despite my objections."
    "I can't deny it was delicious, though."
    "Afterwards, we make way for the school."
    scene bg club_day with dissolve_scene_full
    show sayori 1a at t21
    show monika 1a at t22
    m "Hi, [player]!"
    m "...and Sayori..."
    show sayori at t11
    show monika at thide
    hide monika
    "Monika lets out a deep sigh before heading to the closet, presumably to grab something."
    s "I wonder what that was about?"
    mc "Yeah, weird."
    s "Anyways, what do you want to do?"
    mc "Well, I was going to wait and make sure everything was okay here first--"
    "Monika suddenly calls out from the closet."
    m "Hey, Natsuki, I can't find this thing I'm looking for. You're the only other person who roots through the closet, so can you help me find it?"
    show natsuki 1a at t31
    n "I guess..."
    show natsuki at thide
    hide natsuki
    "She heads off to the closet to help Monika."
    s "That's weird. Usually, she'd say what she was looking for."
    mc "Maybe it's a surprise?"
    s "Maybe, but she would have told me."
    s "Unless..."
    s "...it's a super secret!"
    mc "Maybe, but I don't know."
    # uh oh spaghetti-os, here's our first death
    # for each character's death, delete their file, then play the sound and do the thing
    # character deletion is commented out for the time being since I'm still working on this
    # $ delete_character("natsuki")
    play sound "/mod_assets/sfx/shot.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0
    mc "What was that?"
    m "Woops, I accidentally broke a shelf. My bad!"
    mc "O...kay..."
    m "Oh, there it is! Hey, Yuri, you're pretty tall, maybe you can grab this from the top shelf?"
    show yuri 1a at t33
    y "Sure..."
    show yuri at thide
    hide yuri
    "Yuri heads over to the closet."
    mc "How do you break one of those shelves? Aren't they made out of metal?"
    m "Uh, very carefully, [player]. Very carefully."
    mc "That's {i}hilarious{/i}, Monika. Where do you get your jokes, {i}the back of a Laffy Taffy?{/i}"
    s "Don't be mean to Monika, she's trying her best."
    mc "She's {i}breaking{/i} a {i}metal{/i} shelf."
    mc "How do you {i}do{/i} that?"
    # $ delete_character("yuri")
    play sound "/mod_assets/sfx/shot.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0
    m "Uh, like that, I guess."
    m "Sayori, can we have a chat? President to Vice President?"
    "Sayori starts to head over to the closet, but I stop her."
    mc "Sayori, I don't think she's breaking a metal shelf. Those sounded like gunshots."
    mc "Haven't you noticed that Natsuki and Yuri haven't reappeared from the closet?"
    s "[player], you're being paranoid. Did you stay up late last night watching horror movies again?"
    mc "Sayori, I'm serious, please don't go."
    mc "I would hate to see something happen to you..."
    if sayori_confess:
        mc "{i}Especially since, y'know, we just started dating yesterday...{/i}"
        "I whisper that last part, since I don't want to tell {i}everyone{/i} just yet."
    else:
        mc "We've been friends for so long..."
    mc "Can't you just trust me?"
    s "There's nothing to be afraid of. It's just Monika, after all."
    show sayori at thide
    hide sayori
    "And just like that, she's gone."
    s "Wha--{nw}"
    $ _history_list.pop(-1)
    # $ delete_character("sayori")
    play sound "/mod_assets/sfx/shot.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0
    s "Wha--{fast}"
    "Like, {i}gone{/i} gone."
    "I decide to investigate for myself."
    "Allan, please add more details." # this is where I'll pick up writing next time I get a boost of motivation.

    return

