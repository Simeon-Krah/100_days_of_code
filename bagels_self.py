# coding bagels game offhand
import random

max_digits = 3 # maximum number of digits
max_guesses = 10 # maximum number of times player can guess

# function to generate secret numbers
def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers) # shuffle the list to generate random digits

    secret_num = ""   # empty string to hold secret numbers
    for i in range(max_digits):
        secret_num += numbers[i]

    return secret_num


# function to give clues to player
def get_clues(guess, secret_num):

    if guess == secret_num:
        return "You got it. Well done!"

    clues = [] # empty list to hold clues
    for i in range(len(guess)):

        # return Fermi if player's guess is at the same position as the secret num
        if guess[i] == secret_num[i]:
            clues.append("Fermi")

        # return Pico if player's guess is in the secret number but at a wrong position
        elif guess[i] in secret_num:
            clues.append("Pico")

        # else:
            # clues.append("Bagels")

    # return bagels if guess is entirely wrong
    if len(clues) == 0:
        return "Bagels"

    # sort clues in alphabetical order so not to make it easy for players
    else:
        clues.sort()
        return " ".join(clues)
        # return clues


# main game loop
while True:
    print(f"""I've thought of a {max_digits}-digit number with no repeated digits.
    Try to guess to win the game, but here are some clues for you.
    When I say              It means
    Pico                    One digit is correct, but at wrong position
    Fermi                   One digit is correct and at right position
    Bagels                  No digit is correct""")

    secret_num = get_secret_num()

    print(f"You have {max_guesses} times to guess the secret number")

    current_guess = 1 # initialize current guess time

    # keep looping until maximum guess time is reached
    while current_guess <= max_guesses:

        guess = ""  # empty string to hold guess

        # keep looping until they enter a valid guess
        not_valid_guess = 0
        while len(guess) != max_digits or not guess.isdecimal():
            print(f"Guess time {current_guess}")
            guess = input("> ")
            not_valid_guess +=1

            if not_valid_guess >2:
                print(f"You have exhausted your guesses at guess time {current_guess}. Please enter {max_digits}-digit number")
                break

        clues = get_clues(guess, secret_num)
        print(clues)
        current_guess +=1

        if guess == secret_num:
            break  # player is correct, game over

        if current_guess > max_guesses:
            print(f"Sorry, you have ran out of guess times. The correct answer was {secret_num}")


    print("Do you want to play again? (yes or no)")
    if not input("Answer here: ").lower().startswith("y"):
        break

print("Thanks for playing.")

