define p = Character("Principal Adam", color="#c8ffc8")
define m = Character("Me", color="#c8c8ff")
define s = Character("Soup", color="#8ddde2")
define sx = Character("Sixbutton", color="#53ad64")
define mk = Character("Maikas", color="#824895")

label start:
    python:
        names = ["soup", "sixbutton", "manticron", "maikasavaila", "ana", "kobo", "adam", "gadget", "six", "maikas", "ian", "manti", "clinkerboot", "clinker", "clink", "jelly", "soa", "skylar", "sky", "grant", "brennan", "speakerofamerica"]
        name = renpy.input("What is your name?")
        name = name.strip()
        namel = name.lower()

        if name == " " or name == "":
            name = "Jelly"

        if namel in names:
            taken = True
        
        else:
            taken = False
        
    if taken == True:
        "That name is already taken"
        jump start

label exposition:

    scene hallway
    with fade

    show principal adam at truecenter
    with dissolve

    p "So how is everything at Arcea High, [name]?"

menu:
    "Good":
        jump good
    
    "Bad":
        jump bad


label good:
    m "Good, sir."
    p "Good to hear."
    p "Would you like your schedule?"
    m "Yes sir"
    p "Alright, first you have history with Mr. Manti"
    p "Next, you have English with Ms. Ana and French with Mr. Kobo"
    p "Lastly you have mathematics with Mrs. Jemima"
    p "Understood?"
    
    menu:
        "Yes":
            m "Yes sir"

        "No":
            m "No sir"

label bad:
    m "Actually, it's been pretty rough."
    p "Oh, that was supposed to be retorical, but uhh..."
    p "Let me give you your schedule"
    p "First you have history with Mr. Manti"
    p "Next, you have English with Ms. Ana and French with Mr. Kobo"
    p "Lastly you have mathematics with Mrs. Jemima"
    p "Understood?"

    menu:
        "Yes":
            m "Yes sir"

        "No":
            m "No sir"


    hide principal adam
    with dissolve

    show soup unfocus at center
    with moveinbottom

    show six unfocus at right 
    with moveinright

    show maikas unfocus at left
    with moveinleft

    hide soup unfocus
    show soup at center
    with zoomin

    s "What're you doin here smigger"
    m "What? I'm not even blu-"
    s ""


