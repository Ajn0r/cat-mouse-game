def check_input(letter, wanted):
    """
    Takes the players input and checks it
    """
    if letter == "":
        print("You must enter something")
        return False
    else:
        print(f"You must enter a valid input, {wanted}, please try again")
        return False


def start_game():
    """
    Ask if the player want to start the game
    """
    play = True
    while play:
        start = input("\nAre you ready to play? y/n\n")
        if start.lower() == "y":
            print("Lets play")
            return False
        if start.lower() == "n":
            print("Bye!")
            return False
        while start.lower() != "y" or "n":
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
        " closer to the mouse\n\n")
    start_game()


welcome()
