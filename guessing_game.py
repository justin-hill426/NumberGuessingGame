import random
from statistics import mean, median, mode

"""
1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
"""


def start_game():
    high_score = float('inf')
    play_again = ""
    STARTNUMBER = 1
    ENDNUMBER = 10
    tries = 1
    attempts = []
    printIntro()
    random_number = generateRandomNumber(STARTNUMBER, ENDNUMBER)
    while play_again != 'n':
        if play_again != '':
            print(f"The HIGHSCORE is {high_score}. Can you beat it?")
            random_number = generateRandomNumber(STARTNUMBER, ENDNUMBER)
            play_again = ''
            tries = 1
        try:
            user_guess = int(input(f"Pick a number between {STARTNUMBER} and {ENDNUMBER}: "))
            if user_guess == random_number:
                print(f"\n You got it! It took you {tries} tries\n")
                attempts.append(tries)
                printStatistics(attempts)
                if tries < high_score:
                    high_score = tries
                play_again = input("Would you like to play again? (y/n): ").lower()
                while play_again != 'y' and play_again != 'n':
                    play_again = input("Invalid Input! Please enter a 'y' (to play again) or 'n' (to quit the game): ")
            elif user_guess <= ENDNUMBER and user_guess > random_number:
                tries += 1
                print("Too high. Try again.")
            elif user_guess >= STARTNUMBER and user_guess < random_number:
                tries += 1
                print("Too low. Try again.")
            else:
                raise Exception("The number you entered is outside the range")
        except ValueError as ve:
            print('Please enter a valid integer')
        except Exception as err:
            print(err)
    printGoodbye()


def generateRandomNumber(startRange, endRange):
    return random.randint(startRange, endRange)


def printIntro():
    print("--------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("--------------------------------")


def printGoodbye():
    print("\n--------------------------------")
    print("Thanks for playing the Number Guessing Game! See you next time!")
    print("--------------------------------")


def printStatistics(attempts):
    print("=+=Overall Statistics=+=")
    print(f"Mean: {round(mean(attempts), 2)} tries")
    print(f"Median: {median(attempts)} tries")
    print(f"Mode: {mode(attempts)} tries")
    print()
# Kick off the program by calling the start_game function.


if __name__ == '__main__':
    start_game()
