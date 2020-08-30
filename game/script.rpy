# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define e = Character("Narrator")
define boss = Character("Max")
define kaneki = Character("Kaneki Ken")
define farright = Position(xpos=0.89)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")    
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene home

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show test

    # These display lines of dialogue.

    e "Max wurde geboren als der big GAE"

    e "Wilkommen bei Max Life the AnimationTM"

    menu:
        "Was soll ich jetzt sagen?"

        "Was soll ich hier?":
            "Bitte beende das Spiel."
        
        "End my life.":
            "Goodnight girl i see you tomorrow"

    #Hier kommt der Bosskampf

    scene bg lava

    
    show boss sprite 
    show hpbar at topleft
    play music "<from 153 to 254>boss.mp3" fadein 2.0
    show boss sprite at farright


    boss "DU BIST ALSO DIE MAUER AUF DER LAUER"
    boss "JETZT KANN ICH DICH ENDLICH IN DEN TOPF STECKEN UND KOCHEN"

    menu: 
        e "Wer ist der uLow denn?"

        "Weirdflex.":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound ded
            $renpy.music.set_volume(1.0, 0, 'music')
            #music.set_volume(volume, delay=1, channel="music") 
            "Komischer Winkelschleifer, aber ok."                   

        "Weirdflex big":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound ded
            $renpy.music.set_volume(1.0, 0, 'music') 
            boss "Ganz komischer flex."

        "Sie ist einfach lesbisch":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound ded
            $renpy.music.set_volume(1.0, 0, 'music')
            boss "All woMEN are queens."                   

        "Du kleiner Splasher":
            $renpy.music.set_volume(0.7, 0, 'music')
            play sound ded
            $renpy.music.set_volume(1.0, 0, 'music')
            boss "If she breaths she is a THOT."
    
    scene bg lava with flash        
   
    boss  ":("
    
    e "So endete der Kampf gegen Max."
    e "Ende."
    stop music 

    #Back to Basics
    scene buschei with vpunch   
    scene buschei with hpunch
    $renpy.music.set_volume(1.0, 0, 'music')
    play music "bigsad.mp3" 
    

    show kaneki
    kaneki "Jetzt kriegst du's mit mir zu tun"


    # This ends the game.

    return
