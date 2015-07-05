# word reverser
# takes a users word and prints it out backwards

print(
"""
  
         Welcome to the Word Reverser!

     Enter a word and using black magic we shall
               reverse it for you.

       Press enter to exit the program

"""
)

# set a variable to the whatever the users input is
user_word = input('\nWhat is your word? ')


# create a loop so user can enter and print out words multiple times
while user_word != "":
    reverse_word = user_word[::-1].lower() # using slices print out reverse
    print(reverse_word.title())
    user_word = input('\nWhat is your word? ') # Asks for new word

print('\nThanks for playing')
                  

                  
#simple
