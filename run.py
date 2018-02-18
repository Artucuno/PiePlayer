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
          "l. Load Songs (from Playlist)\n"
          "\n"
          "w. Find Songs on the web")
    choice = user_choice()
    if choice == "l":
        subprocess.call(("python", "play.py"))
    if choice == "w":
        webbrowser.open("https://ganna.com")

main()

