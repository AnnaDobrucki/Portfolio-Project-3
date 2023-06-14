### Takes functions from utility.py, and imports creds ###

from utility import clear_screen, draw_hangman, random, string, gspread, os, time, user_lost, user_win
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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
points = 0
print(f"here are {points}")


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
                        print(Fore.GREEN + "▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▒█░▒█ █▀▀█ █▀▀▄ █▀▀▀ █▀▄▀█ █▀▀█ █▀▀▄")
                        print(Fore.GREEN + "▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ▒█▀▀█ █▄▄█ █░░█ █░▀█ █░▀░█ █▄▄█ █░░█")
                        print(Fore.GREEN + "▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▒█░▒█ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀ \n")
                        break

            elif ready == "N":
                    clear_screen()
                    print("That's a shame, come on back when you're ready...")

        except ValueError as value_error:
                print(value_error)
    
username = ''
def username():
    """
    Function to add username for use in scoreboards
    """
    while True:
        username = input("Give us a name for the scoreboard! \n")

        if username.isalnum() is not True:
            clear_screen()
            print(Fore.RED + "Sorry we need letters and numbers for this one!")
            continue

        else:
            clear_screen()
            print(Fore.BLUE + f"Hi {username}, you must guess the word within 6 goes or loose a limb each loss. \n")
            input("Let's get going! Please press enter and see how many letters there are to guess...")
            return username

def pick_random_word():
    """
    Create a list of random words to be guessed for user
    """
    WORDS = ("python", "javascript", "needed", "hangman", "answer", "celestial", "piano", "dragons", "stars", "ring", "green")
    word = random.choice(WORDS)
    return word.upper()

def replay():
    ### Replay function to allow user to end or try again with game ###
    while True:
        try:
            replay = input(" \nWould you like to try again? Enter Y/N").upper()
            if replay == "Y":
                clear_screen()
                hidden_word = pick_random_word()
                play_game(hidden_word)

            elif replay not in ("Y","N"):
                raise ValueError("Oops, please answer with Y or N!")

            else:
                clear_screen()
                print("Well thanks for playing! Have a lovely day.")
                break

        except ValueError as value_error:
                print(value_error)

def play_game(hidden_word):
    ### Function to start playing the game and show the length of the hidden word###
    picked_word = list(hidden_word)
    global points

    print(Fore.BLUE + " \n The length of the word is below")
    print(len(hidden_word) * "_ ")
    word_arragement = "_" * len(hidden_word)
    guessed = []
    correct_answers = []
    lives_remaining = 6 
    tries = False

    while tries is False and lives_remaining > 0:
        try:
            answers = input("\n Time to guess a letter, what'll it be this time? \n").upper()
            time.sleep(1)
            clear_screen()
            if answers.isalpha() and len(answers) == 1:
                if answers in guessed:
                    raise ValueError ("\n Fraid not, you already tried that!")
                    time.sleep(2)
                    clear_screen()
            ### Checks user answers and iterrates through to see if word has been completed ###
                elif answers in picked_word:
                    print(f"\n Smashing it out the park! KEEP GOING! \n ")
                    guessed.append(answers)
                    correct_answers.append(answers)
                    print(f"So far you have guessed these correct letters {correct_answers}")
                    hidden_word_list = list(word_arragement)
                    indices = [i for i, letter in enumerate(hidden_word) if letter == answers]
                    for index in indices:
                        hidden_word_list[index] = answers
                    word_arragement = "".join(hidden_word_list)
                    if "_" not in word_arragement:
                        tries = True
                    
            ### Checks if user entered wrong letter and keeps track of lives, until == 0 ###        
                elif answers not in hidden_word:
                    guessed.append(answers)
                    lives_remaining -= 1
                    print(f"Ouch so close and yet so far, you loose a limb! You have {lives_remaining} tries remaining! \n")
                    draw_hangman(lives_remaining)
                    print(f"So far you have used these {guessed}")
                
            else:
                raise ValueError(Fore.YELLOW + "Hang on we need only one letter, and remember no numbers either!")
        except ValueError as value_error:
                print(value_error)
        ### Printing the answers onto screen for user ###
        current = ""
        if tries is False:
            for letter in hidden_word:
                if letter in answers:
                    current += letter
                else:
                    current += " _"
            print(current)
            
    ### If statement for win/ loose outcomes ###
    if tries:
        clear_screen()
        user_win()
        points += 10 
        print(f"You were right the answer was {hidden_word}!")
        replay()
        return points

    if lives_remaining == 0:
        clear_screen()
        user_lost()
        points -= 10 
        print(f"Oops you lost this time! In'm afraid the word we were looking for was {hidden_word}")
        replay()
        return points
        


def update_score(all_points):
    score.append_row(all_points)
    print(f"Test this")

def main():
    beginning_intro()
    username()
    pick_random_word()
    hidden_word = pick_random_word()
    all_points = play_game(hidden_word)
    update_score(all_points)
    

main()

