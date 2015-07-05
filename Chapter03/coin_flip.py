# this program flips a coin 100 times and displays the result to the user

import random

#intialise counters
counter = 0
headsCount = 0
tailsCount = 0
heads = 1
tails = 2

#Greet user to the program

print("\tWelcome to the Coin Flip program")

print("\nThis program flips a coin 100 times and displays the results.")
input("Press enter to run the program. ")

while counter < 100:
    flip = random.randint(1,2)
    if flip == heads:
        headsCount += 1
        counter += 1
    elif flip == tails:
        tailsCount += 1
        counter += 1
    else:
        continue

print("\n\nThat didn't take long! After 100 flips there was", headsCount,"heads"\
      " and", tailsCount,"tails!")
input("\nPress enter key to exit. ")
