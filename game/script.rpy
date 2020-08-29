#test kommentar1
# The script of the game goes in this file.
#testkommentar2

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
define boss = Character("Max")

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
    play music "<from 153 to 294>boss.mp3" fadein 1.0 loop

    boss "DU BIST ALSO DIE MAUER AUF DER LAUER"
    boss "JETZT KANN ICH DICH ENDLICH IN DEN TOPF STECKEN UND KOCHEN"

    menu: 
        "Wer ist der uLow denn?"

        "Weirdflex.":
            stop music
            play sound "ded.mp3"
            "Komischer Winkelschleifer, aber ok."                   

        "Weirdflex big":
            stop music  
            play sound "ded.mp3"
            "Ganz komischer flex."
            
            

    boss "Ok. :("

    e "So endete der Kampf gegen Max."
    e "Ende."

    # This ends the game.

    return
