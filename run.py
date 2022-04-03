from curses.ascii import isalpha


def check_input(letter):
    """
    Takes the players input and checks it
    """
    if letter == "":
        print("You must enter something")
        return False
    elif not isalpha(letter):
        print("You must enter a valid letter from the alphabeth")
        return False
    else:
        print("You must enter a valid input")
        return False


def start_game():
    """
    Ask if the player want to start the game
    """
    play = True
    while play:
        start_game = input("\tAre you ready to play? y/n\n")
        while start_game.lower() != "y" or "n":
            check_input(start_game)
            break
        if start_game.lower() == "y":
            print("Lets play")
            return False
        elif start_game.lower() == "n":
            print("Bye!")
            return False


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
        " closer to the mouse\n\n")
    start_game()


welcome()
