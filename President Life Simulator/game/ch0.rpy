init python:
    import time
    from sys import exit as SysExit    
    class RelationshipObject:
        def __init__(self):
            self.jerry = 20
            self.presa = 10
            self.dev = 30
        
##All var define statements in here
define char = Character("You") 
define p = Character("Presa") #Daughter
define j = Character("Jerry") #Assistant
define relationships = RelationshipObject()
define hasPhone = True
################################
##Audio definitions
define audio.creepy = "audio/bensound-creepy.mp3"
define audio.breathe = "audio/envato breathe.mp3"
###################

label start:
    ##Init debug stuff
    call _setup_debug_file
    call _debug_check
    ##Start of actual scene
    scene office
    "You are the president. You are sitting at your desk, doing nothing useful at all."
    "It's your job to be a  good figurehead for the government that gives people hope. As one would imagine, you don't do that."
    "Currently, you are waiting for your personal assisstant, Jerry, to finish a special mission of yours:"
    "To get you a Breakfast Burrito."
    "The problem is, he's taking quite a long time."
    "Would you rather go out and look for him or wait?"
    menu:
        "Wait":
            jump wait_jerry
        "Go look for him":
            jump look_jerry
##Branch for waiting for Jerry
label wait_jerry:
    "You wait."
    "And you wait."
    "And you continue to wait."
    "You wait for two hours. It is lunchtime."
    "Jerry arrives."
    show jerry
    with fade
    "Jerry walks in, holding a frozen burrito."
    j "Hey boss!"
    j "I got your breakfast! I've just got to heat it up!"
    menu:
        "Accept":
            jump accept_burrito
        "Decline Politely":
            jump decline_burrito_polite
        "Decline Rudely":
            jump decline_burrito_rude
        "Decline Aggressively":
            jump decline_burrito_aggressive

label accept_burrito:
    char "Thank you, Jerry, but what took so long?"
    j "Sorry, boss, but I was busy, as my daughter-"
    char "Oh, nevermind. I don't care."
    j "Oh.... sorry, boss..."
    $ relationships.jerry -= 1
    char "Whatever. I've got work to do. Heat it up and then get out."
    "Jerry looks like he's about to cry as he heats up your burrito."
    "It's finished."
    "Jerry leaves."
    jump jerry_leaves_ch0

label decline_burrito_polite:
    char "No thank you, Jerry. I'm not hungry anymore."
    j "But you sure, boss? I got your favorite-"
    char "YES, Jerry. I am sure."
    j "O-okay, boss..."
    "Jerry leaves, looking very dissapointed."
    $ relationships.jerry -= 2
    jump jerry_leaves_ch0

label decline_burrito_rude:
    char "No, Jerry. I don't want your late as hell burrito."
    j "Oh, sorry bout that boss, I just was-"
    char "I do not care."
    char "Leave."
    "Jerry nearly cries as he runs out of the door."
    $ relationships.jerry -= 5
    jump jerry_leaves_ch0

label decline_burrito_aggressive:
    char "NO."
    char "I DON'T WANT YOU OR YOUR BURRITO JERRY."
    char "YOU ARE THE LARGEST DISSAPOINTMENT IN MY LIFE."
    char "NOW GET OUT."
    $ relationships.jerry -= 5
    "And jerry left as quickly as he showed up."
    jump jerry_leaves_ch0

label jerry_leaves_ch0:
    hide jerry
    with fade
    "While you continue to sit and do nothing with your life, you hear someone knock on your door."
    "Should you let them in?"
    menu:
        "Let them in:"
            jump end_of_demo
        "Don't":
            jump end_of_demo



##############################################################
##Branch for going to look for him
label look_jerry:
    scene hallway
    "You walk out into the hallway to look for Jerry."
    "After some walking, you seem to have reached a fork in the hallway."
    "Which direction will you go in?"
    menu:
        "Right":
            jump look_jerry_right0
        "Left":
            jump look_jerry_left0

label look_jerry_right0:
    scene big-meeting-room
    "You go right."
    "You end up in a large room with many windows."
    "What will you do?"
    menu:
        "Jump out of the window":
            jump ending_window_jump
        "Ask around for jerry":
            jump ask_around_jerry

label look_jerry_left0:
    "You go left."
    "It's another hallway. What will you-"
    "{i}ring ring.{/i}"
    "It's your phone. Your daughter is calling."
    "Pick it up? (Note: don't)"
    menu:
        "Don't pick it up":
            $ relationships.presa -= 3
            "Good choice. Nobody likes her anyways."
        "Pick it up":
            call phone_presa0
            "That's what I thought."
        "Throw your phone at the wall":
            "You throw your phone at the wall."
            "It is smashed into a million pieces."
            $ hasPhone = False
            $ relationships.presa -= 3
    "Anyways, continue down the hallway or go back?"
    menu:
        "Go back":
            jump back_to_office_ch0
        "Keep going":
            jump look_jerry_left_keep_going

label phone_presa0:
    "...really? Are you sure?"
    menu:
        "No":
            return
        "No":
            return

label look_jerry_left_keep_going:
    "You decided to keep going."
    "You walk around for quite a while. In fact, you are walking around for two hours until you reach the exit."
    "Go outside?"
    scene door-hallway
    menu:
        "Yes":
            jump go_outside_ch0
        "No":
            jump no_oustide_ch0
        "U2F2ZSB5b3VyIGRhdWdodGVy":
           play music breathe
           $ relationships.dev -= 10
           scene dev face1
           call _do_creepy_dialogue("You cannot U2F2ZSB5b3VyIGRhdWdodGVy") 

label no_outside_ch0:
    "After coming this far, you decide that exposing yourself to natural light is not worth it."
    "You turn around, but you can't really remember which direction you came from."
    "Which is it?"
    menu:
        "Left":
            jump ending_shot_left
        "Right":
            jump back_to_office_ch0

label back_to_office_ch0:
    scene office
    "You make it back to your office."
    "You notice that there are two notes on your desk."
    "One is yellow and one is red."
    "Which will you read first?"
    menu:
        "Red":
            jump end_of_demo
        "Yellow":
            jump end_of_demo