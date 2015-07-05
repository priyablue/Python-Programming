# fortune cookie simulator
# picks a fortune at random and displays it for the user


# imports random module

import random

# picks the number for the fortune

fortune = random.randint(1, 5)


print("\tWelcome to the Fortune Cookie Simulator")

input("\nPress enter key to see your fortune. \n")

# depending on the number generated one of these fortunes will print

if fortune == 1:
    print("People are naturally attracted to you.")
elif fortune == 2:
    print("You learn from your mistakes... You will learn a lot today.")
elif fortune == 3:
    print("If you have something good in your life, don't let it go!")
elif fortune == 4:
    print("What ever you're goal is in life, embrace it visualize it," \
          " and for it will be yours.")
elif fortune == 5:
    print("Your shoes will make you happy today.")


print("\nPress enter key to exit.")
