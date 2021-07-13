"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

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
    high_score = None
    play_again = ""
    STARTNUMBER = 1
    ENDNUMBER = 10
    tries = 0
    print("--------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("--------------------------------")
    random_number = random.randint(STARTNUMBER, ENDNUMBER)
    while play_again != 'n':
        if high_score:
            print(f"The HIGHSCORE is {high_score}")
        user_guess = int(input(f"Pick a number between {STARTNUMBER} and {ENDNUMBER}: "))
        if user_guess == random_number:
            print(f"/n You got it! It took you {tries}")
        elif user_guess <= ENDNUMBER and user_guess > :
            print("It is lower")






# Kick off the program by calling the start_game function.
start_game()