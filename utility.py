import random
import string
import gspread
import os
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def clear_screen():
    """
    Function to clear screen
    """
    os.system('clear')


def draw_hangman(lives_remaining):
    """
    Hangman visual according to lives remaining.
    """
    if lives_remaining == 6:
        print(Fore.YELLOW + '''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========''')
    elif lives_remaining == 5:
        print(Fore.MAGENTA +
              '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
    elif lives_remaining == 4:
        print(Fore.LIGHTBLUE_EX +
              '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
    elif lives_remaining == 3:
        print(Fore.BLUE +
              '''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''')
    elif lives_remaining == 2:
        print(Fore.LIGHTRED_EX +
              '''
                +---+
                |   |
                O   |
               /|\\  |
                    |
                    |
                =========''')
    elif lives_remaining == 1:
        print(Fore.CYAN +
              '''
                +---+
                |   |
                O   |
               /|\\  |
               /    |
                    |
                =========''')
    elif lives_remaining == 0:
        print(Fore.RED +
              '''
                +---+
                |   |
                O   |
               /|\\  |
               / \\ |
                    |
                =========''')


def user_lost():
    print(Fore.RED + '''
                ▒█░░▒█ █▀▀█ █░░█ 　 ▒█░░░ █▀▀█ █▀▀ ▀▀█▀▀ █
                ▒█▄▄▄█ █░░█ █░░█ 　 ▒█░░░ █░░█ ▀▀█ ░░█░░ ▀
                ░░▒█░░ ▀▀▀▀ ░▀▀▀ 　 ▒█▄▄█ ▀▀▀▀ ▀▀▀ ░░▀░░ ▄ \n''')


def user_win():
    print(Fore.GREEN + '''

                ▒█░░▒█ █▀▀█ █░░█ 　 ▒█░░▒█ █▀▀█ █▀▀▄
                ▒█▄▄▄█ █░░█ █░░█ 　 ▒█▒█▒█ █░░█ █░░█
                ░░▒█░░ ▀▀▀▀ ░▀▀▀ 　 ▒█▄▀▄█ ▀▀▀▀ ▀░░▀ \n''')
