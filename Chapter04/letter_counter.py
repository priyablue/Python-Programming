# prints the amount of letters in a word entered by the user§


print ('Welcome to the Letter Counter 3000. Type \'exit\' to end the program')

word = input("\nWhat is the word you wish to know how many letters are in? ")

while not word == "exit":
    count = 0
    word = input("Next word? ")

    for letter in word:
        count +=1
    print(count)

print ('\nThanks for using Letter Counter 3000. Have a pleasant day')
