from utility import clear_screen, draw_hangman, random, string, gspread, os
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
            if ready not in ("Y","N"):
                    raise ValueError("Oops, please answer with Y or N!")
            if ready == "Y":
                        print("Awesome, let's get started \n")
                        clear_screen()
                        print("▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▒█░▒█ █▀▀█ █▀▀▄ █▀▀▀ █▀▄▀█ █▀▀█ █▀▀▄")
                        print("▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ▒█▀▀█ █▄▄█ █░░█ █░▀█ █░▀░█ █▄▄█ █░░█")
                        print("▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▒█░▒█ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀")
                        break
                        # MAKE SURE TO ADD FUNCTION TO START GAME
            elif ready =="N":
                    clear_screen()
                    print("That's a shame, come on back when you're ready...")
        except ValueError as value_error:
                print(value_error)
    

beginning_intro()

def username():
    while True:
        username = input("Give us a name for the scoreboard! \n")

        if username.isalnum() is not True:
            print("Sorry we need letters and numbers for this one!")
            continue
        else:
            print(f"Hi {username}, you must guess the word within 6 goes or loose a limb each loss.")
            input("Let's get going! Please press enter")
            return username

username()

def pick_random_word():
    WORDS = ("python", "javascript", "needed", "carrying", "answer", "celestial", "piano", "dragons")
    word = random.choice(WORDS)
    return word.upper()

hidden_word = pick_random_word()
print(hidden_word)


def play_game(hidden_word):
    picked_word = set(hidden_word)
    guess = []
    lives = 6 
    while True:
        try:
            answers = input("\n Time to guess a letter, what'll it be this time? \n").upper()
            if answers in guessed:
                raise ValueError ("\n Fraid not, you already tried that!")
            if answer in picked_word:
                clear_screen()
        except ValueError as value_error:
                print(value_error)

