define e = Character("Narrator")
define boss = Character("Max")
define kaneki = Character("Kaneki Ken")
define farright = Position(xpos=0.89)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")    
transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

label start:
    #################### Prolog ####################
    scene image "bgs/home.jpg"
    show image "sprites/test.png"
    e "Max wurde geboren als der big GAE"
    e "Wilkommen bei Max Life the AnimationTM"
    e "Mafi2 ergibt mehr Sinn als dieser Anfang"

    menu:
        "Was soll ich jetzt sagen?"
        "Was soll ich hier?":
            "Bitte beende das Spiel."   
            jump kanekikampf
        "End my life.":
            "Goodnight girl i see you tomorrow"

    #################### Bosskampf Max ####################
    scene image "bgs/lava.png"
    show image "sprites/boss sprite.png" at farright
    show image "sprites/hpbar.png" at topleft
    play music "<from 153 to 254>audio/bgs/boss.mp3" fadein 2.0
    boss "DU BIST ALSO DIE MAUER AUF DER LAUER"
    boss "JETZT KANN ICH DICH ENDLICH IN DEN TOPF STECKEN UND KOCHEN"
    menu: 
        e "Wer ist der uLow denn?"
        "Weirdflex":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound "audio/effects/ded.mp3"
            $renpy.music.set_volume(1.0, 0, 'music')
            #music.set_volume(volume, delay=1, channel="music") 
            "Komischer Winkelschleifer, aber ok."                   
        "Flammenpeitsche":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound "audio/effects/bruh.mp3"
            $renpy.music.set_volume(1.0, 0, 'music')    
            stop music 
            boss "Das ist kein Anime..."
            with vpunch
            with hpunch
            e "Das wars WeebSlayerMove200xxEndMeHAHAHxDDD."
            play sound "audio/effects/mario.mp3"
            e "Rest in pepperoni."
            return
        "Sie ist einfach lesbisch":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound "audio/effects/ded.mp3"
            $renpy.music.set_volume(1.0, 0, 'music')
            boss "All woMEN are queens."                   
        "Du kleiner Splasher":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound "audio/effects/ded.mp3"
            $renpy.music.set_volume(1.0, 0, 'music')
            boss "If she breaths she is a THOT."
    scene image "bgs/lava.png" with flash        
    boss  ":("
    e "So endete der Kampf gegen Max."
    e "Ende."
    stop music 

    #################### Bosskampf Kaneki ####################
    label kanekikampf:
    scene image "bgs/buschei.png" 
    with hpunch
    with vpunch
    play music "audio/bgs/bigsad.mp3"
    show image "sprites/kaneki.png"
    kaneki "Jetzt kriegst du's mit mir zu tun !"
    kaneki "Wenn du denkst Frau Rose war schlimm ich mach genauso schlimm und noch schlimmer"
    kaneki "Watch dis"
    show image "sprites/kaneki.png" at shake
    pause 1.0
    hide image "sprites/kaneki.png"
    show image "sprites/kanekit.png"
    kaneki "Stell dir vor Leute benutzen das als Profilbild."
    menu:
        e "Warum passt das Bild so gut mit dem Regen in den Hintergrund?"
        "Idk clicc here to find out":
            show longboi at topleft with squares
            boss "Was soll mir das jetzt sagen?"
    e "Bruh"
    show longboi with dissolve:
         zoom 4.0
    boss "..."
    boss "Oh"
    boss "Ich glaube ich erkenne da ein Muster"
    boss "Zoom noch bisschen mehr rein."
    e "Bruh"
    show longboi with dissolve:
        xpos 0.0 ypos -0.5 zoom 8.0
    e "Ich zieh mir ne Line kein Bock mehr"
    boss "NEIN WARTE !!"
    stop music
    boss "ER IST ES !!"
    hide image "sprites/kanekit.png" with dissolve
    hide longboi with dissolve
    with fade
    show back with flash
    play music "audio/bgs/yujiro.mp3" 
    e "o.o"
    # This ends the game.
    return
