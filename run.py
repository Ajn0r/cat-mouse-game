def welcome():
    """
    Welcomes the player, runs once game is started.
    """
    play = True
    while play:
        print(
            "\t***********************************\n"
            "\t Welcome to the cat and mouse game!\n"
            "\t***********************************\n\n"
            "Can you save the mouse from the cat?\n"
            "I will think of a word and you'll guess it,"
            " one letter at a time\n"
            "For every wrong guess the cat gets one step"
            " closer to the mouse\n\n")

        start_game = input("\tAre you ready to play? y/n\n")
        if start_game.lower() == "y":
            print("Lets play")
        elif start_game.lower() == "n":
            print("Bye!")
            play = False
        else:
            print("Dont understand")


welcome()
