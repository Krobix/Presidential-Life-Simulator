label _setup_debug_file:
    python:
        if not persistent.debug_file_set:
            with open("debug_c.txt", "w") as f:
                f.write("0\n")
            persistent.debug_file_set = True
    return

label _debug_check:
    python:
        try:
            with open("debug_c.txt", "r") as f:
                debugContent = f.read()
            err = False
        except:
            err = True

    if err:
        call _do_error(0)
        
    elif debugContent == "1\n" or debugContent == "1":
        jump _debug_screen

    elif debugContent == "0\n" or debugContent == "0":
        return

label _debug_screen:
    scene placeholder bg
    menu:
        "exec":
            $ inputx = renpy.input("enter exec input")
            $ exec(inputx)

label _do_creepy_dialogue(txt):
    while True:
        window show
        $ time.sleep(0.5)
        window hide
        $ time.sleep(0.5)
        "[txt]"

label _do_error(errcode):
    if errcode == 0:
        scene err file
        window hide

    "Error code [errcode]"
    $ SysExit()