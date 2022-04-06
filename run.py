import random
import time
from words import hard_words, easy_words
from graphic import cat_and_mouse


guesses = []
wrong_guesses = []


def check_input(letter, wanted):
    """
    Takes the players input and checks it, the function takes the input
    as letter, and wanted is what the program is asking for.
    Function can be used for every descision.
    """
    if letter == "":
        print("You must enter something")
        return False
    else:
        print(f"You must enter a valid input, {wanted}")
        return False


def play_again(name):
    """
    Once the game is finished, asks the player
    if they would like to play again
    """
    print(
        f"Thank you for playing {name}!\n"
        "I hoped you enjoyed it!\n")
    one_more_time = input("Would you like to play again? y/n\n")
    if one_more_time.lower() == "y":
        print("Lets play")
        display_game(name)
    if one_more_time.lower() == "n":
        print(
            f"I guess this is it for now then {name}!"
            "\nSee you next time!")
        exit()
    else:
        check_input(start_game, "y to play again, any other key to exit game")
        last_chance = input()
        if last_chance.lower() == "y":
            display_game(name)
        else:
            exit()


def show_game(word):
    """
    Displays the game board
    """
    for letter in word:
        # if the letter has been guessed, this will display it.
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            # prints an _ for every letter in the word
            print("_", end=" ")


def display_game(name, word):
    """
    Displayes the game and generates
    a random word to be guesses
    """
    allowed_errors = 7
    done = False
    while not done:
        show_game(word)
        # lets the player take a guess
        guess = input("\nEnter your guess: \n")
        # check if input is larger than 0 and not more than one
        if len(guess) == 0 and len(guess) > 1:
            print("You can only enter one letter at a time")
        # check if the guessed letter already has been guessed
        elif guesses.__contains__(guess.lower()):
            print(f"You have already guessed {guess}")
        # if the input not is in the aplhabeth
        elif not guess.isalpha():
            print("You can only enter a letter from the alphabeth")
        else:
            guesses.append(guess.lower())
            if guess.lower() not in word:
                wrong_guesses.append(guess)
                print(f"Oh no, {guess} is not in the word!")
                print(f"You have guessed: {', '.join(wrong_guesses)}\n")
                allowed_errors -= 1
                print(cat_and_mouse[len(wrong_guesses)])
            else:
                print(f"Great job {name}, {guess} is in the word!\n")

            if allowed_errors > 1:
                print(f"You have got {allowed_errors} guesses left!")
            if allowed_errors == 1:
                print("This will be your last guess, use it wisely!")
                time.sleep(0.7)
            if allowed_errors == 0:
                break
            done = True
            for letter in word:
                if letter.lower() not in guesses:
                    done = False
    if done:
        print("You found the word and saved the mouse!")
    else:
        print(
            f"Oh no! What have you done {name}!\n"
            "Well I guess the cat is happy anyway!\n"
            f"The word i was thinking of was {word}\n"
            "  ~~ Better luck next time! ~~\n\n"
            )
    wrong_guesses.clear()
    guesses.clear()
    random.shuffle(word)
    play_again(name)


def difficulty(name):
    """
    Player choose at which level of
    difficulty they would like to play
    """
    print(
        "You will have 7 guesses at the word im thinking of"
        "Would you like me to think of:"
        "1: an easy word? or"
        "2: A hard word?"
        )
    level = input("Choose 1 for easy and 2 for hard")
    if level == 1 or "easy":
        word = random.choice(easy_words)
        display_game(name, word)
    elif level == 2 or "hard":
        word = random.choice(hard_words)
        display_game(name, word)
    else:
        print("You must choose a valid option")


def ask_name():
    """
    Ask the player for a name, if they don't input anything
    they will be asked if they are sure, if still no entry
    a name will be randomly generated for them.
    """
    name = input("What is your name?\n")
    if name == "":
        print(
            "Oops, lookes like you did't enter anything..."
            "\nLets try again!")
        name_try_again = input("What is your name?\n")
        if name_try_again == "":
            name_list = [
                'Allan', 'Snowdrop', 'Charmayanne', 'Leonardo',
                'Hubert', 'Anderson', 'Marelow', 'Brielle', "Bob"]
            random_name = random.choice(name_list)
            print(
                "If you don't want to tell me your name, it's okey!\n"
                "I guess I will just give you I name I like!\n"
                "Hmm let me think..."
                )
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.8)
            print(
                f"I've got it! I'll just call you {random_name}!\n")
            return random_name
        return name_try_again
    return name


def start_game():
    """
    Ask if the player want to start the game,
    """
    play = True
    while play:
        start = input("\nAre you ready to play? y/n\n")
        if start.lower() == "y":
            print("Lets play\n")
            name = ask_name()
            difficulty(name)
            return False
        if start.lower() == "n":
            print("Bye!")
            return False
        # If the user inputs something other than y or n
        # they will end up in this loop.
        while start.lower() != "y" or start.lower() != "n":
            check_input(start_game, "y or n")
            break


def welcome():
    """
    Welcomes the player, runs once game is started.
    """

    print(
        "\t***********************************\n"
        "\t Welcome to the cat and mouse game!\n"
        "\t***********************************\n\n"
        "Can you save the mouse from the cat?\n"
        "I will think of a word and you'll guess it,"
        " one letter at a time\n"
        "For every wrong guess the cat gets one step"
        " closer to the mouse\n")
    start_game()


welcome()
