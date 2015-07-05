# Critter Caretaker
# A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = random.randint(0,5), boredom = random.randint(0,5)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __str__(self):
        rep = "Name: {}\nHunger: {}\nBoredom: {}".format(self.name, 
                                                         self.hunger, 
                                                         self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        while True:
            try:
                food = int(input("How much would you like to feed {}? ".format(self.name)))
                break
            except ValueError:
                print("Please enter a number.")
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        while True:
            try:
                food = int(input("How long would you like to play with {}? ".format(self.name)))
                break
            except ValueError:
                print("Please enter a number.")
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    while True:
        try:
            amount = int(input("How many critters would you like? "))
            break
        except ValueError:
            print("Please enter a number.")
    
    crit_list = []
    
    for crit in range(amount):
        name = input("What is the name of critter {}: ".format(crit+1))
        critter = Critter(name)
        crit_list.append(critter)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            for critter in crit_list:
                critter.talk()
        
        # feed your critter
        elif choice == "2":
            for critter in crit_list:
                critter.eat()
         
        # play with your critter
        elif choice == "3":
            for critter in crit_list:
                critter.play()
            
        # print out a critter
        elif choice == "4":
            for critter in crit_list:
                print(critter)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
