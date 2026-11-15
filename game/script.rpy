# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Claire", color= "#ffcccc")
define a = Character("Andrew", color= "#ffcccc")

# The game starts here.

label start:


    scene bg dimstreet

    show claire annoyed

    # These display lines of dialogue.

    c "We're done."

    show andrew sad

    a "NO CLAIRE! I swear i'll change! I promise!"

    menu:
        "Chase after her":
            jump chaseafterher

        "Go home":
             jump gohome

label chaseafterher:
    
    show andrew reaching

    a "Wait! Don't go please!"

    show claire pitiful

    c "I'm sorry Andrew, goodbye."

    scene bg dimstreet 

    with Dissolve(1.0)

    scene bg dimstreet

    a "I still can't believe it. I have to find a way to get her back."

    a "Wait what's that? Is this a Wish Willow? I heard about these things. They can grant wishes."

    show andrew holdingwishwillow

    a "I wish for Claire to only love me for eternity."

    show andrew snappingwishwillow

    show andrew wishwillowsparkle

    a "What am I doing. This probably won't even work. I'm just going to get some rest"

    scene bg dimstreet
    
    with Dissolve(1.0)

    scene bg aroom

    play sound "bgm/doorknock.ogg"

    a "Who could possible be knocking at this hour?"

   menu:
    "Open the door":
        jump openDoor

    "Ignore the knocking":
        jump ignore

label openDoor:

    a "Whatever I'm just going to open the door."

    scene bg door

    pause 0.5

    scene bg dooropen

    play sound "bgm/dooropen.ogg"

    show claire joyful

    c "Andrew! I missed you so much! It's been so long since we last saw each other."

    show andrew groaning

    a "What? Claire? How did you get here? I thought you left me."
    
    show claire joyful

    c "What do you mean silly? I never left you."

    show andrew frightened

    a "..."

    show claire smile

    play sound "bgm/adrenaline.ogg"

    c "I love you Andrew. I always have and I always will."

    show andrew confused

    a "Whatever let's just go to bed. I have a lot of work to do tomorrow."

    show claire joyful

    c "Okay Andrew. Goodnight."

    scene bg doorclose
with Dissolve(1.0)

return

    scene bg aroom

    show andrew closingeyes

    a "I'm just going to ignore it. They probably have the wrong house."

    play sound "bgm/doorknock.ogg"

    a "Can they just go away already? I'm exhausted and I just want to sleep."

    play sound "bgm/dooropen.ogg"

    show andrew asleep

    scene bg aroom

    with Dissolve(1.0)

    pause 2.5

    scene bg aroomm

    play sound "bgm/yawn.ogg"

    a "I wonder what happened last night. I'm gonna go check the front door."

    with Dissolve(1.0)

    scene bg door
    show andrew calm

    play sound "bgm/dooropen.ogg"

    scene bg dooropen
    
    show andrew calm
    
    scene bg doormat

    show andrew confused

    a "What is this? A note? What does it say?"

    scene bg note

    "I love you Andrew. I won't stop loving you. I'll be back soon. -Claire"

    show andrew confused

    a "What does this mean? Whatever, I guess I'll just go to work. I have a lot to do today."

    scene bg aroomm

    with Dissolve(1.0)

    scene bg officenight

    show andrew working

    a "And... done. Finally I can go home."

    scene bg officenight

    with Dissolve(1.0)

    a "I wonder if I should walk home or take the bus today."

label walkhome:

    scene bg dimstreet
    
    show andrew walking

    a "Why do i feel as if... someone is following me...?"

    show andrew skeptical

    a "Whatever. Probably just my imagination. I should hurry up and get home."

    play sound "bgm/thump.ogg"

    show andrew shocked

    a "What was that!?"

    show claire smileharsh

    c "I told you I would find you Andrew. You can't run away from me."

    show andrew scared

    a "Claire? You're scaring me right now. Why do you have a bat?"

    show claire smileharsh

    c "If I can't have you, no one can."

    scene bg black

    play sound "bgm/impact.ogg"

    "POW"

    scene bg dimstreet

    show claire smilebloos

    c "I told you I would find you. Goodbye Andrew."

    scene bg dimstreet

    with Dissolve(1.0)

    jump bad_ending

label bad_ending:

    scene bg black

    "Andrew's story ends here."

    return



label gohome:

    show andrew hands

    a "I have to fix this. I can't live without her."

    scene bg dimstreet

    with Dissolve(1.0)

    scene bg aroom

    "Andrew is about to go to sleep."

    show andrew tired

    a "I guess I'll have to hope for the best and wait for her to come back, there's nothing else I can do."

    play sound "bgm/yawn.ogg"

    scene bg aroom

    with Dissolve(1.0)

    scene bg aroomm

    show andrew sleeping

    play sound "bgm/doorknock.ogg"

    a "Huh? Who could possibly be knocking?"

    show andrew confused

    a "Whatever it's about time to get up either way."

    show bg door

    show andrew calm

    play sound "bgm/dooropen.ogg"

    show bg dooropen

    show claire awkward

    c "Andrew I thought about it and I feel like I made a mistake. Let's give our relationship another chance?"

    show andrew happy

    a "I would love that Claire."

    "Andrew and Claire lived happily ever after."

    "The End."

    return
