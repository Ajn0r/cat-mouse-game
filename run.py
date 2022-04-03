import random
import time


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
    print(f"Well done {name}!")
    one_more_time = input("Would you like to play again? y/n")
    if one_more_time.lower() == "y":
        print("Lets play")
        # Should go to display_game later
        display_game(name)
    if one_more_time.lower() == "n":
        print(f"Thank you {name} for playing!")
        exit()
    else:
        check_input(start_game, "y to play again, any other key to exit game")
        last_chance = input()
        if last_chance.lower() == "y":
            # Should go to display game later
            start_game()
        else:
            exit()


def display_game(name):
    """
    Displayes the game and generates 
    a random word to be guesses
    """
    print(f"{name} here the game will be displayed!")
    return False


def ask_name():
    """
    Ask the player for a name, if they don't input anything
    they will be asked if they are sure, if still no entry
    a name will be randomly generated for them.
    """
    name = input("what is your name?\n")
    if name == "":
        print("oops, lookes like you did't enter anything...")
        name_try_again = input("What is your name?\n")
        if name_try_again == "":
            name_list = ['Allan', 'Marie', 'Rose', 'Leonardo']
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
                f"I've got it! I'll just call you {random_name}!")
            return random_name
        else: 
            return name_try_again
    else:
        return name


def start_game():
    """
    Ask if the player want to start the game,
    """
    play = True
    while play:
        start = input("\nAre you ready to play? y/n\n")
        if start.lower() == "y":
            print("Lets play")
            name = ask_name()
            print(name)
            play_again(name)
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
