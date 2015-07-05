# Modified Guess My Number program
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 goes\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


def main():
    """Loops and asks for user to guess number"""
    global guess, tries
    while not tries >= 10:
        if guess == the_number:
            print("You guessed it!  The number was", the_number)
            print("And it only took you", tries, "tries!\n")
            break
        elif guess > the_number:
            print("Lower...")
        elif guess < the_number:
            print("Higher...")
        else:
            print("That's not a number. ")
        guess = ask_number("What's your next guess? ", 1, 100)
        tries += 1

# starts the game
main()

if tries >= 10:
    print("You took too many guesses")
    
  
input("\n\nPress the enter key to exit.")
