import random
import string
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('Creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman_P_3')

score = SHEET.worksheet("Scoreboard")

data = score.get_all_values()
print(data)

def beginning_intro():
   while True:
    try:
        ready = input("\nAhoy there folks! You ready to play some hangman? --> Y/N?").upper()
        if ready == "Y":
                    print("Awesome, let's get started")
                    break
                    # MAKE SURE TO ADD FUNCTION TO START GAME
        elif ready =="N":
                print("That's a shame, come on back when you're ready...")
    except LetterError:
        print("Oops, please answer with Y or N!")

beginning_intro()

                    
def pick_random_word():
    WORDS = ("python", "javascript", "needed", "carrying", "answer", "celestial", "piano")
    word = random.choice(WORDS)
    return word.upper()

hidden_word = pick_random_word()
print(hidden_word)

def answer(hidden_word):
    picked_word = set(hidden_word)
