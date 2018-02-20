# PiePlayer (c) ArtGames101 2018
import pygame, sys, os, subprocess, time
import random
import config

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    print("Choose a song!\n")
    subprocess.call(("dir", "songs"))
    choice = user_choice()
    clear_screen()
    print("Playing Song... [{}]\n"
          "\n"
          "CTRL + C Exit".format(time.ctime()))
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("songs/{}".format(choice))
        pygame.mixer.music.play()
    except:
        clear_screen()
        input("Unable to play/load a song!")
        main()
    while pygame.mixer.music.get_busy() == True:
        continue
    main()


main()
