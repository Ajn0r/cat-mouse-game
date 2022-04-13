import random
import time
from words import hard_words, easy_words
from graphic import cat_and_mouse, mouse


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
    one_more_time = input("Would you like to play again? y/n\n")
    if one_more_time.lower() == "y":
        print("Lets play")
        difficulty(name)
    if one_more_time.lower() == "n":
        print(
            "Thank you for playing!\n"
            "I hoped you enjoyed it!\n")
        exit()
    else:
        check_input(start_game, "y to play again, any other key to exit game")
        last_chance = input()
        if last_chance.lower() == "y":
            difficulty(name)
        else:
            print(
                "Thank you for playing!\n"
                "I hoped you enjoyed it!\n")
            exit()


def allow_guess(allowed_errors, guess):
    """
    Checks how many allowed errors
    the player has left to decide if the
    get to make another guess
    """
    if allowed_errors > 1:
        print(f"Oh no, {guess} is not in the word!\n")
        print(f"You have got {allowed_errors} guesses left\n")
        return True
    if allowed_errors == 1:
        print("This will be your last guess, use it wisely!\n")
        time.sleep(0.7)
        return True
    if allowed_errors == 0:
        return False


def display_game(name, word):
    """
    Handels guesses and displays the game
    """
    allowed_errors = 7
    done = False
    while not done:
        show_word(word)
        # lets the player take a guess
        guess = input("\n\nEnter your guess: \n")
        # check if input is larger than one
        if len(guess) > 1:
            print("You can only enter one letter at a time")
        # check if the input is larger than 0 (not blank)
        elif guess == "":
            print("Oops, you must enter a letter")
        # check if the guessed letter already has been guessed
        elif guesses.__contains__(guess.lower()):
            print(f"You have already guessed {guess}")
        # if the input not is in the aplhabeth
        elif not guess.isalpha():
            print("You can only enter a letter from the alphabet")
        else:
            guesses.append(guess.lower())
            if guess.lower() not in word:
                allowed_errors -= 1
                print(cat_and_mouse[len(wrong_guesses)])
                wrong_guesses.append(guess)
                guesses_left = allow_guess(allowed_errors, guess)
                if guesses_left is False:
                    break
                print(f"You have guessed: {', '.join(wrong_guesses).lower()}")
            else:
                print(
                    f"Great job {name},"
                    f" your guess: {guess} is in the word!\n")
                print(mouse[1])
            done = True
            for letter in word:
                if letter.lower() not in guesses:
                    done = False
        print(
            "_______________________________"
            "________________________________"
            "\n_______________________________"
            "________________________________\n")
    # if the player finds the word and wins
    if done:
        print(
            f"Congratulations {name}!\n"
            "You found the word and saved the mouse!\n")
        print(mouse[0])
    # Game over
    else:
        print(
            f"Oh no! What have you done {name}!\n"
            "Well, I guess the cat is happy anyway!\n\n"
            f"The word I was thinking of was {word}\n\n"
            "  ~~ Better luck next time! ~~\n\n"
            )
    # reset the lists containg guesses
    wrong_guesses.clear()
    guesses.clear()
    play_again(name)


def show_word(word):
    """
    Displays the letter of the words
    As underscores, if the letter is not guessed
    otherwise the correct letter.
    """
    for letter in word:
        # if the letter has been guessed, the letter will be displayed
        # instead of an _
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            # prints an _ for every letter in the word
            print("_", end=" ")


def difficulty(name):
    """
    Players choose at which level of
    the difficulty they would like to play
    """
    decision = True
    print(
        "\n\t\tHow to play:\n"
        "\nYou will have 7 guesses at the word I'm thinking of\n"
        "Would you like me to think of an easy or hard word?\n"
        )
    while decision:
        level = input("Choose e for easy and h for hard\n")
        # If player choose easy level, generates word from easy word list
        if level.lower() == "e":
            word = random.choice(easy_words)
            print(
                f"Good choise {name},\n"
                "Super hard word coming up!\n...")
            time.sleep(1)
            print("Just kidding! Easy it is!\n")
            time.sleep(0.8)
            print(
                "I think this one is not too hard!\n"
                f"The word im thinking of contains {len(word)} letters\n")
            display_game(name, word)
        # If player choose hard level, generate word from hard word list
        if level.lower() == "h":
            word = random.choice(hard_words)
            print(
                f"Feeling confindent are we {name}?\n"
                "I'm not gonna make this easy for you!\n")
            time.sleep(0.6)
            print("Give me a sec to come up with a good one...")
            time.sleep(1)
            print("...\n")
            time.sleep(0.8)
            print(
                "Alright I will be impressed if you crack this one!\n"
                f"The word I'm thinking of contains {len(word)} letters\n"
                "Good luck!\n")

            display_game(name, word)
        # If player fails to enter a valid input
        while level != "e" or level != "h":
            check_input(level, "e or h")
            break


def ask_name():
    """
    Ask the player for a name, if they don't input anything
    they will be asked if they are sure, if still no entry
    a name will be randomly generated for them.
    """
    name = input("\nWhat is your player name?\n").strip()
    # If player fails to enter anything first time, they get one more chance
    if name == "":
        print(
            "Oops, looks like you didn't enter anything..."
            "\nLet's try again!")
        name_try_again = input("What is your name?\n").strip()
        # If the player fails to enter something the second time
        # they will be given a random name
        if name_try_again == "":
            name_list = [
                'Allan', 'Snowdrop', 'Charmayanne', 'Leonardo',
                'Hubert', 'Anderson', 'Marelow', 'Brielle', "Bob"]
            random_name = random.choice(name_list)
            print(
                "If you don't want to tell me your name, it's okey!\n"
                "\nI guess I will just give you I name I like!\n"
                "Hmm let me think..."
                )
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.8)
            print(
                f"I've got it! I'll just call you {random_name}!\n")
            # Returns randomly generated name if player
            # fails to enter anything twice
            return random_name.capitalize()
        # Returns name if player enters their name on second try
        return name_try_again.capitalize()
    # Returns name if entered correctly first time
    return name.capitalize()


def start_game():
    """
    Ask if the player want to start the game,
    """
    play = True
    while play:
        start = input("\nAre you ready to play? y/n\n")
        if start.lower() == "y":
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
        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  Welcome to Save the mouse!
                               ___
                      _  _  .-'   '-.
                     (.)(.)/         \\
                     /^ ^             ;
                    o_\\-mm-......-mm`~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                Can you save the mouse from the cat?
            I will think of a word and you'll guess it,
                        one letter at a time.
             For every wrong guess, the cat gets one step
                        closer to the mouse.
        """)
    start_game()


welcome()
