# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
hint_guess = 0
score = 0

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
     Enter 'hint' if you need some help
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    if guess == "hint":
        if correct == "python":
            print('Snaaaaake')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
        elif correct == "jumble":
            print('This game...')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
        elif correct == "easy":
            print('It\'s not very hard')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
        elif correct == "difficult":
            print('It\'s not that easy')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
        elif correct == "answer":
            print('I can\'t exactly give you the answer')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
        elif correct == "xylophone":
            print('An instrument')
            guess = input("Your guess: ")
            hint_guess +=1
            continue
    else:
        print("Sorry, that's not it.")
        guess = input("Your guess: ")
    
if guess == correct:
    print("\nThat's it!  You guessed it!")

print("Thanks for playing.")

if hint_guess:
    print('\nYou used', hint_guess,' hints. No points for you.')
else:
    score += 300
    print('\nYou scored', score,' points. Well done.')
    

input("\n\nPress the enter key to exit.")
