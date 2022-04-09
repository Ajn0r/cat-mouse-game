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
        "\tThank you for playing!\n"
        "\tI hoped you enjoyed it!\n")
    one_more_time = input("\tWould you like to play again? y/n\n")
    if one_more_time.lower() == "y":
        print("\tLets play")
        difficulty(name)
    if one_more_time.lower() == "n":
        print(
            f"\tI guess this is it for now then {name}!"
            "\n\tSee you next time!")
        exit()
    else:
        check_input(start_game, "y to play again, any other key to exit game")
        last_chance = input()
        if last_chance.lower() == "y":
            difficulty(name)
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


def allow_guess(allowed_errors, guess):
    """
    Checks how many allowed errors
    the player has left to decide if the
    get to make another guess
    """
    if allowed_errors > 1:
        print(f"\tOh no, {guess} is not in the word!\n")
        print(f"\tYou have got {allowed_errors} guesses left\n")
        return True
    if allowed_errors == 1:
        print("\tThis will be your last guess, use it wisely!\n")
        time.sleep(0.7)
        return True
    if allowed_errors == 0:
        return False


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
        guess = input("\n\n\tEnter your guess: \n")
        # check if input is larger than 0 and not more than one
        if len(guess) == 0 or len(guess) > 1:
            print("\tYou can only enter one letter at a time")
        # check if the guessed letter already has been guessed
        elif guesses.__contains__(guess.lower()):
            print(f"\tYou have already guessed {guess}")
        # if the input not is in the aplhabeth
        elif not guess.isalpha():
            print("\tYou can only enter a letter from the alphabeth")
        else:
            guesses.append(guess.lower())
            if guess.lower() not in word:
                allowed_errors -= 1
                print(cat_and_mouse[len(wrong_guesses)])
                wrong_guesses.append(guess)
                guesses_left = allow_guess(allowed_errors, guess)
                if guesses_left is False:
                    break
                print(f"\tYou have guessed: {', '.join(wrong_guesses)}")
            else:
                print(f"\tGreat job {name}, {guess} is in the word!\n")
            done = True
            for letter in word:
                if letter.lower() not in guesses:
                    done = False
        print(
            "\n---------------------------------------------------\n")
    if done:
        print("\t\nYou found the word and saved the mouse!\n")
    else:
        print(
            f"\tOh no! What have you done {name}!\n"
            "\tWell I guess the cat is happy anyway!\n\n"
            f"\tThe word i was thinking of was {word}\n\n"
            "\t  ~~ Better luck next time! ~~\n\n"
            )
    wrong_guesses.clear()
    guesses.clear()
    play_again(name)


def difficulty(name):
    """
    Player choose at which level of
    difficulty they would like to play
    """
    decicion = True
    print(
        "\n\tHow to play: "
        "\n\tYou will have 7 guesses at the word im thinking of\n"
        "\tWould you like me to think of an easy or hard word?\n\n"
        )
    while decicion:
        level = input("\tChoose e for easy and h for hard\n")
        if (level) == "e":
            word = random.choice(easy_words)
            display_game(name, word)
        if (level) == "h":
            word = random.choice(hard_words)
            display_game(name, word)
        while level != "e" or level != "h":
            check_input(level, "e or h")
            break


def ask_name():
    """
    Ask the player for a name, if they don't input anything
    they will be asked if they are sure, if still no entry
    a name will be randomly generated for them.
    """
    name = input("\n\tWhat is your player name?\n")
    if name == "":
        print(
            "\tOops, lookes like you did't enter anything..."
            "\n\tLets try again!")
        name_try_again = input("\tWhat is your name?\n")
        if name_try_again == "":
            name_list = [
                'Allan', 'Snowdrop', 'Charmayanne', 'Leonardo',
                'Hubert', 'Anderson', 'Marelow', 'Brielle', "Bob"]
            random_name = random.choice(name_list)
            print(
                "\tIf you don't want to tell me your name, it's okey!\n"
                "\tI guess I will just give you I name I like!\n"
                "\tHmm let me think..."
                )
            time.sleep(0.5)
            print("\t...")
            time.sleep(0.5)
            print("\t...")
            time.sleep(0.8)
            print(
                f"\tI've got it! I'll just call you {random_name}!\n")
            return random_name
        return name_try_again
    return name


def start_game():
    """
    Ask if the player want to start the game,
    """
    play = True
    while play:
        start = input("\n\tAre you ready to play? y/n\n\t")
        if start.lower() == "y":
            name = ask_name()
            difficulty(name)
            return False
        if start.lower() == "n":
            print("\tBye!")
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
        "\tCan you save the mouse from the cat?\n"
        "\tI will think of a word and you'll guess it,\n"
        "\t one letter at a time\n"
        "\tFor every wrong guess the cat gets one step\n"
        "\t closer to the mouse\n\n")
    start_game()


welcome()
