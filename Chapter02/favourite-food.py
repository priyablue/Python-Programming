# User enters two favourite foods
# the program then returns a concatination of the two

name = input("Hi there, what's your name? ")

print("\nHi,", name)

foodOne = input("\nWhat is one of your favourite foods? ")
print("Awesome!", foodOne, "is delicious")

foodTwo = input("\nWhat is your second favourite food? ")
print("Mmmm, I love", foodTwo,"too! have you ever thought of trying", \
      foodOne + foodTwo,"?")

input("\n\nPress Enter to exit")
