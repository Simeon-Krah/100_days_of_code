# Write your code here :-)
"""Day 1 of Python projects from Al Sweigart's book
Other than stated, codes are writen by self after
looking and understanding the author's own.
The bagels game asks user to guess 3 digits,
string in this case, and compares them with
a secret number."""
import random

num_digits = 3 # number of digits of the secret number
max_guesses = 10 # maximum times player can guess

def main():
    print("""I'm thinking of a {}- digit number with no
    repeated digit. Try to guess the number, but here are some clues for
    you.
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    For example, if the secret number was 248, and your guess
    was 843, the clue would be
    Fermi Pico""".format(num_digits))

    # main game loop
    while True:
        # stores the secret number the player has to guess
        secret_num = get_secret_num()
        print("I have thought of a number")
        print("You have {} times to guess the number to win the game".format(max_guesses))

        # ask the user to guess as far us they haven't reached the max guess times
        num_guesses = 1
        while num_guesses <= max_guesses:

            # keep looping until they enter a valid guesss
            guess = ""
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess number {}".format(num_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses +=1

            if guess == secret_num:
                break  # player is correct, so out of game

            if num_guesses > max_guesses:
                print("Sorry, you have run out of time. The correct was {}".format(secret_num))

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break

    print("Thanks for playing.")


def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(num_digits):
        secret_num += str(numbers[i])

    return secret_num


def get_clues(guess, secret_num):
    """ print Pico, Fermi and Bangels to guide players,
    but they are sorted in alphabetical order so not to
    make it simple for players"""

    if guess == secret_num:
        return "You got it. Well done!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")

        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"

    else:
        clues.sort()
        return "".join(clues)


if __name__ == "__main__":
    main()


