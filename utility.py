import random
import string
import gspread
import os
import time

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
        print('''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========''')
    elif lives_remaining == 5:
        print(
            '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
    elif lives_remaining == 4:
        print(
            '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
    elif lives_remaining == 3:
        print('''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''')
    elif lives_remaining == 2:
        print('''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========''')
    elif lives_remaining == 1:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========''')
    elif lives_remaining == 0:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========''')
