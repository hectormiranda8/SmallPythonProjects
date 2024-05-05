"""
In Bagels, a deductive logic game, you 
must guess a secret three-digit number 
based on clues. The game offers one of 
the following hints in response to your guess: 
“Pico” when your guess has a correct digit in the 
wrong place, “Fermi” when your guess has a correct 
digit in the correct place, and “Bagels” if your guess 
has no correct digits. You have 10 tries to guess the 
secret number.
"""


import random


def initialComment() -> None:
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:\tThat means:")
    print("Pico\tOne digit is correct but in the wrong position.")
    print("Fermi\tOne digit is correct and in the right position.")
    print("Bagels\tNo digit is correct.")


def continuePlaying() -> bool:
    print("Do you want to play again? (yes or no)")
    user_input = input("> ").lower()
    while user_input != "yes" and user_input != "no":
        user_input = input("> ").lower()
    return user_input == "yes"


def verifyGuess(num_to_guess: dict[str, int], user_input: dict[str, int]) -> bool:
    if num_to_guess == user_input:
        print("You got it!")
        return True

    hint_str = ""
    for k in user_input.keys():
        for gk in num_to_guess.keys():
            if k == gk:
                if user_input[k] == num_to_guess[gk]:
                    hint_str += "Fermi "
                else:
                    hint_str += "Pico "
                num_to_guess.pop(gk, None)
                break
    if len(hint_str) == 0:
        print("Bagels")
    else:
        print(hint_str)
    return False


def bagels() -> None:
    guess_count = 0

    guessed_number = str(random.randint(100, 999))
    guessed_number_dict = {y:x for x, y in enumerate(guessed_number)}
    print("\nI have thought up a number.")
    print("\tYou have 10 guesses to get it.")

    while guess_count < 10:
        print(f"Guess #{guess_count}:")
        user_input = {y:x for x, y in enumerate(input())}
        if verifyGuess(guessed_number_dict.copy(), user_input):
            break
        guess_count += 1

    if guess_count == 10:
        print("Oops... you've run out of guessess. Good luck next time!")
    
    
    if continuePlaying():
        bagels()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    print("Bagels, a deductive logic game.")
    print("By Al Sweigart al@inventwithpython.com\n")

    initialComment()
    bagels()