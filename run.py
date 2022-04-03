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
            " closer to the mouse")
        play = False


welcome()
