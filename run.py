# PiePlayer (c) ArtGames101 2018
import pygame, sys, os, subprocess, webbrowser

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
    print("PiePlayer\n"
          "================")
    print("\n"
          "l. Play Songs\n"
          "\n"
          "w. Find Songs on the web")
    choice = user_choice()
    if choice == "l":
        clear_screen()
        print("PiePlayer Audio\n"
              "===================")
        print("\n"
              "1. Play Playlist (Python)\n"
              "\n"
              "2. Play A Song (Python 3)\n"
              "\n"
              "i. Info\n"
              "0. Back")
        choice = user_choice()
        if choice == "1":
            subprocess.call(("python", "play.py"))
        if choice == "2":
            subprocess.call((sys.executable, "playr.py"))
        if choice == "i":
            clear_screen()
            print("PiePlayer Audio\n"
                  "===================")
            print("\n"
                  "Playlist:\n"
                  "The Playlist is looped and shuffled!\n"
                  "\n"
                  "Play Song:\n"
                  "Choose a song to play (is not looped)")
            input("\n"
                  "Back")
            main()
    if choice == "w":
        webbrowser.open("https://ganna.com")
        print("Opening Please wait...")
        time.sleep(5)
        main()

main()

