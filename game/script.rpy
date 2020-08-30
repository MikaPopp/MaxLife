define e = Character("Narrator")
define boss = Character("Max")
define kaneki = Character("Kaneki Ken")
define farright = Position(xpos=0.89)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")    

label start:
    #################### Prolog ####################
    scene image "bgs/home.jpg"
    show image "sprites/test.png"
    e "Max wurde geboren als der big GAE"
    e "Wilkommen bei Max Life the AnimationTM"
    menu:
        "Was soll ich jetzt sagen?"
        "Was soll ich hier?":
            "Bitte beende das Spiel."     
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
    scene image "bgs/buschei.png" 
    with hpunch
    with vpunch
    play music "audio/bgs/bigsad.mp3"
    show image "sprites/kaneki.png"
    kaneki "Jetzt kriegst du's mit mir zu tun"
    
    
    # This ends the game.
    return
