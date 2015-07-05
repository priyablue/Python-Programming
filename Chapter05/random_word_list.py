# this program prints a list of words in a random order
# without repeating any

import random

# constant list of words and empty list for used words

WORDS = ("Tweet", "Python", "Programming", "Learning", "Skip")
used_words = []


print("This program prints a list of words in a random order without repeating"\
      "\nany of them.")
input("\nPress enter to see what I can do")

while len(used_words) != len(WORDS):
    word = random.choice(WORDS)
    if word not in used_words:
        print(word)
        used_words.append(word)

input('\nPress enter to exit')
