from utility import clear_screen, draw_hangman, random, string, gspread, os, time
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
    """
    Start to game with an intro and choice wether to play or not
    """
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
                        print("▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▒█░▒█ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀ \n")
                        break
            elif ready =="N":
                    clear_screen()
                    print("That's a shame, come on back when you're ready...")
        except ValueError as value_error:
                print(value_error)
    

beginning_intro()

def username():
    """
    Function to add username for use in scoreboards
    """
    while True:
        username = input("Give us a name for the scoreboard! \n")

        if username.isalnum() is not True:
            clear_screen()
            print("Sorry we need letters and numbers for this one!")
            continue
        else:
            clear_screen()
            print(f"Hi {username}, you must guess the word within 6 goes or loose a limb each loss. \n")
            input("Let's get going! Please press enter and see how many letters there are to guess...")
            return username

name = username()

def pick_random_word():
    """
    Create a list of random words to be guessed for user
    """
    WORDS = ("python", "javascript", "needed", "carrying", "answer", "celestial", "piano", "dragons")
    word = random.choice(WORDS)
    return word.upper()

hidden_word = pick_random_word()
print(hidden_word) 
"""REMOVE AFTER BUILDING PLAYGAME FUNC"""


def play_game(hidden_word):
    picked_word = list(hidden_word)
    print(len(hidden_word) * "_ ")
    guessed = []
    correct_answers = []
    lives_remaining = 6 
    tries = False
    while tries is False and lives_remaining > 0:
        try:
            answers = input("\n Time to guess a letter, what'll it be this time? \n").upper()
            time.sleep(1)
            clear_screen()
            if answers.isalpha and len(answers) == 1:
                if answers in guessed:
                    raise ValueError ("\n Fraid not, you already tried that!")
                    time.sleep(2)
                    clear_screen()

                elif answers in picked_word:
                    print(f"\n Smashing it out the park {name} \n ")
                    guessed.append(answers)
                    correct_answers.append(answers)
                    print(f"So far you have guessed these correct letters {correct_answers}")
                    
                elif answers not in hidden_word:
                    guessed.append(answers)
                    lives_remaining -= 1
                    print(f"Ouch so close and yet so far, you loose a limb! You have {lives_remaining} tries remaining! \n")
                    draw_hangman(lives_remaining)
                    print(f"So far you have used these {guessed}")
                    
            else:
                raise ValueError("Hang on we need only one letter, and remember no numbers either!")
        except ValueError as value_error:
                print(value_error)
        
        if tries:
            print("\n... I didn't expect that to happen, you're not as "
              "dumb as you look. Well done.\n")
    if lives_remaining == 0:
        clear_screen()
        print("You loose \n")
        input("Would you like to try again?")

play_game(hidden_word)
