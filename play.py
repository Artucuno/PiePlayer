# PiePlayer (c) ArtGames101 2018
import pygame, sys, os
import random
import config

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def songloop():
    clear_screen()
    print("Playing a random song...\n"
          "\n"
          "CTRL + C Exit")
    pygame.mixer.init()
    pygame.mixer.music.load("songs/{}".format(random.choice(config.songs)))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    songloop()

songloop()
