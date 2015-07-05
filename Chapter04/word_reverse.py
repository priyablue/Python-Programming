# takes a word from user and prints it out backwards

word = None

print('Welcome to the word reverse program. Press enter to exit')

while word != "":
    word = input('\nWhat word would you like reversed? ')
    print(word[::-1])

print('See you later!')
