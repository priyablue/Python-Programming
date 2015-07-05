import random

WORDS = ("elephant", "pineapple", "cresent")

# computer picks random word from list
word = random.choice(WORDS)

# set number of letter guesses
letter_guesses = 5

print(
"""
                   Welcome to the Word Guessing Game!

    The computer will pick a word at random then tell you how many letters
    are in that word. You then have 5 attempt to see if certain letters are
    in the word. The computer will only respond yes or no then after your
    letter guesses you can attempt to guess the whole word. Good luck!
"""
)

# user is told how many letters are in said word
print('\nThe word has', len(word), 'letters in it.')

# user gets 5 goes to see if certain letters are in the word
# computer only responds yes or no 
while letter_guesses > 0:
    letter_guess = input('Pick a letter: ')
    if letter_guess in word:
        print('Yes.')
        letter_guesses -= 1
        continue
    else:
        print('No.')
        letter_guesses -=1
        continue



# after 5 letter guesses the user must attempt to guess the word

print('\nNow you must attempt to guess the word!')

user_word = input('What is your first guess? ')

while user_word.lower() != word:
    user_word = input('\nSorry that isn\'t the word, try again: ')
    

print ('Well done! You correctly guessed the word.')
