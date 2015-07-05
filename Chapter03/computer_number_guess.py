# welcome to the number picker game
# the user picks a number and the computer has to guess

import random

# user sets number to guess
userNum = int(input("What's your number between 1 and 100 that I have to try"\
                    "and guess?" \
                    "\nGo ahead and type it, honestly I am not looking..."))

# intitalised counters and stuff
guessList = []
computerGuess = ""
guesses = 0

# loop that runs while the computers guess doesn't equal users number


while computerGuess != userNum:
    computerGuess = random.randint(1,100)
    if computerGuess in guessList:
    # if it has used the number before it starts
    # the loop again and picks a new number
        continue
    elif computerGuess == userNum:
    # if the guess matches the users number it breaks the loop
        break
    else:
        print("Is your number", computerGuess,"? No? Let me guess again")
        guessList.append(computerGuess)
        guesses += 1

print("Ah ha! Go it! Your number is", userNum," I knew I'd get it eventually.")
print("It only took me", guesses," tries but I got there!")

input("\nPress enter key to exit. ")
