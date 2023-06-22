# Takes functions from utility.py, and imports creds

from utility import clear_screen, draw_hangman, random,\
     gspread, time, user_lost, user_win
from google.oauth2.service_account import Credentials
import sys
import colorama
from colorama import Fore
colorama.init(autoreset=True)

debug = "--debug" in sys.argv

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


def beginning_intro():
    """
    Start to game with an intro and choice wether to play or not
    """
    while True:
        try:
            ready = input("\nAhoy there folks! You"
                          "ready to play some hangman? --> Y/N? \n").upper()
            if ready not in ("Y", "N"):
                raise ValueError("Oops, please answer with Y or N!")

            if ready == "Y":
                clear_screen()
                print(Fore.GREEN + " ▒█░▒█ █▀▀█ █▀▀▄ █▀▀▀ █▀▄▀█ █▀▀█ █▀▀▄")
                print(Fore.GREEN + " ▒█▀▀█ █▄▄█ █░░█ █░▀█ █░▀░█ █▄▄█ █░░█")
                print(Fore.GREEN + " ▒█░▒█ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀ \n")
                break

            else:
                clear_screen()
                print("That's a shame, come on back when you're ready...")

        except ValueError as value_error:
            print(value_error)


def username():
    """
    Function to add username for use in scoreboards
    """
    global username
    while True:
        username = input("Give us a name for the scoreboard! \n")

        if username.isalnum() is not True:
            clear_screen()
            print(Fore.RED + "Sorry we need letters and numbers for this one!")

        else:
            clear_screen()
            print(Fore.BLUE + f"Hi {username}, you must guess the word within "
                  , Fore.WHITE + "6", Fore.BLUE + "goes or loose a "
                  "limb each loss.\n")
            print(Fore.GREEN + "Make sure to guess a singular letter, and"
                  " don't use a number.\n")
            print(Fore.RED + "Good Luck Muhahahaha! \n")
            input("Let's get going! Please press enter and see how"
                  " many letters there are to guess...\n")
            return username


def pick_random_word():
    """
    Create a list of random words to be guessed for user
    """
    WORDS = ("python", "javascript", "needed", "hangman", "answer",
             "celestial", "piano", "dragons", "stars",
             "ring", "green", "blessing")
    word = random.choice(WORDS)
    if debug:
        print(word)
    return word.upper()


def play_game(hidden_word):
    # Function to start playing the game and show the length of the hidden word
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
            # Creates input option for letters and clears
            # the screen after it has been entered
            answers = input("\n Time to guess a letter, what'll"
                            " it be this time? \n").upper()
            time.sleep(1)
            clear_screen()
            if answers.isalpha() and len(answers) == 1:
                if answers in guessed:
                    raise ValueError(Fore.YELLOW + "\n Fraid not"
                                     ", you already tried that!")
                    time.sleep(2)
                    clear_screen()

# Checks user answers and iterrates through to see if word has been completed #
                elif answers in picked_word:
                    print(Fore.GREEN + "\n Smashing it out the park!"
                          " KEEP GOING! \n ")
                    guessed.append(answers)
                    correct_answers.append(answers)
                    print("So far you have guessed these correct \n")
                    for item in correct_answers:
                        print(item, end=" ")
                    print(Fore.BLUE + "\n Don't stop now!\n")

                    hidden_word_list = list(word_arragement)
                    indices = [i for i, letter in enumerate(hidden_word)
                               if letter == answers]
                    for index in indices:
                        hidden_word_list[index] = answers
                    word_arragement = "".join(hidden_word_list)
                    if "_" not in word_arragement:
                        tries = True
                    print(word_arragement)

# Checks if user entered wrong letter and keeps track of lives, until == 0
                elif answers not in hidden_word:
                    guessed.append(answers)
                    lives_remaining -= 1
                    print(f"Ouch so close and yet so far, you loose a limb!"
                          f" You have {lives_remaining} tries remaining!\n")
                    draw_hangman(lives_remaining)
                    print("So far you have used the words: \n")
                    for item in guessed:
                        print(item, end=" ")
                    print(Fore.BLUE + "\nCare to try again?\n")
                    print(word_arragement)


            else:
                raise ValueError(Fore.YELLOW + "Hang on we need only one"
                                               " letter, and remember no "
                                               "numbers either!")

        except ValueError as value_error:
            print(value_error)

# If statement for win/ loose outcomes
    if tries:
        clear_screen()
        user_win()
        points += 5
        print(f"You were right the answer was {hidden_word}!")
        replay()
        return points

    if lives_remaining == 0:
        clear_screen()
        user_lost()
        points -= 5
        print(f"Oops you lost this time! In'm afraid the word we"
              f" were looking for was {hidden_word}")
        replay()
        return points


def replay():
    # Replay function to allow user to end or try again with game
    response = input(" \nWould you like to try again? Enter Y/N\n").upper()
    if response == "Y":
        clear_screen()
        hidden_word = pick_random_word()
        play_game(hidden_word)

    elif response not in ("Y", "N"):
        clear_screen()
        print(Fore.YELLOW + "Oops, please answer with Y or N!")
        replay()

    else:
        clear_screen()
        print(Fore.BLUE + "Thanks for playing! Have a lovely day.\n")


def update_score(scores, all_points):
    print(f"Here are the points you managed to score! {all_points}")
    score.append_row(scores)


def main():
    beginning_intro()
    name = username()
    hidden_word = pick_random_word()
    all_points = play_game(hidden_word)
    scores = [name, all_points]
    update_score(scores, all_points)


main()
