define p = Character("Principal Adam", color="#c8ffc8")
define m = Character("Me", color="#c8c8ff")
define s = Character("Soup", color="#8ddde2")
define sx = Character("Sixbutton", color="#53ad64")
define mk = Character("Maikas", color="#824895")

python:
    global names
    names = ["soup", "sixbutton", "manticron", "maikasavaila", "ana", "kobo", "adam", "gadget", "six", "maikas", "ian", "manti", "clinkerboot", "clinker", "clink", "jelly", "soa"]

label start:
    python:
        names = ["soup", "sixbutton", "manticron", "maikasavaila", "ana", "kobo", "adam", "gadget", "six", "maikas", "ian", "manti", "clinkerboot", "clinker", "clink", "jelly", "soa"]
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
    p "Excellent to hear, have a nice day young man."

label bad:
    m "Actually, it's been pretty rough."
    p "Well son, let me give you some advice."
    p "Man up pussy."
    hide principal adam
    with dissolve

    show soup at center
    with moveinbottom

    show six at right 
    with moveinright

    show maikas at left
    with moveinleft

    s ""


