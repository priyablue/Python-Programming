# This is a Character Creator program
# it allows the user to spend a set amount of points on atributes
# user can spend points, take points and reassign them too

total = 30
user_input = None
attributes = {"strength": 0, "health": 0, "wisdom": 0, "dexterity": 0}

print("""         Welcome to the Character Creator!

            In this program you have 30 points to spend on four
            different attributes. These attributes are Strength,
                     Health, Wisdom, and Dexterity.

      """)

# while user choice isn't 0 the loop runs
while user_input != 0:
    print("""\nHere are your options:

                 Exit        - 0
                 Add points  - 1
                 Take points - 2
                 See totals  - 3
              """)
    user_input = int(input('\nChoice: '))
    if user_input == 0:
        print('Goodbye and good luck out there...')
    elif user_input == 1:
        attrib = input('What attribute would you like to add points to? ')
        attrib = attrib.lower()
        if attrib in attributes:
            points = int(input('\nHow many points do you want to add? '))
            while points > total:
                print('Sorry you don\'t have that many to spend!')
                points = int(input('\nHow many points do you want to add? '))
            attributes[attrib] = points
            total -= points
        else:
            print('\nSorry that isn\'t a valid selection')
    elif user_input == 2:
        attrib = input('Which attribute would you like to take points from? ')
        attrib = attrib.lower()
        if attrib in attributes:
            points = int(input('\nHow many points would you like to take? '))
            if points > attributes[attrib]:
                total += attributes[attrib]
                attributes[attrib] = 0
                print('\n You had less than', points,'in',attrib.title(),'so all the'\
                      ' points in', attrib.title(),'have been taken and added back to your'\
                      ' total to spend')
            else:
                total += points
                attributes[attrib] -= points
        else:
            print('\nSorry that isn\'t a valid selection')
    elif user_input == 3:
        print('Attribute Totals:\n')
        print('ATTRIBUTE\tPOINTS')
        for attribute, points in attributes.items():
            print(attribute, '\t', points)
        print('Total\t', total)
    else:
        print('\nSorry that isn\'t a valid option')


# let's user exit program
input('Press enter to exit')
                
                     
