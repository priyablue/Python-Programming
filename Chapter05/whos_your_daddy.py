# this program let's user enter a name to find out who their father is
# user is able to search for a name, add a father song pair, replace an
# entry, and delete a father son pair.

son_dict = {"Skip": ("Alan","Jim"), "John": ("Mark", "Tim"),
            "Simon": ("Stephen", "Bob"),}
choice = None

print("""
               Welcome to the Who\'s Your Daddy program.
                    The only place to find out who
                           your daddy is.
 

  You can search using a name to find out who their father or grandfather is,
you can add to the list, update an entry, and even remove an entry from the list.
      """)

while choice != 0:
    print("""
      Options

      Exit                         - 0
      Search for son's father      - 1
      Search for son's grandfather - 2
      Add Entry                    - 3
      Update Entry                 - 4
      Remove Entry                 - 5
      

      """)
    choice = int(input('\nChoice: '))

    if choice == 0:
        print('Goodbye')
        
    elif choice == 1:
        son_name = input('What is the name of the person who\'s father you wish to find? ')
        son_name = son_name.title()
        if son_name in son_dict:
            print('The father of', son_name,'is', son_dict[son_name][0])
        else:
            print(son_name,'isn\'t in the list yet, why don\'t you add it?')

    elif choice == 2:
        son_name = input('What is the name of the son whose grandfather you want to find? ')
        son_name = son_name.title()
        if son_name in son_dict:
            print('\nThe grandfather of', son_name,'is', son_dict[son_name][1])
        else:
            print(son_name,'isn\'t in the list yet, why don\'t you add it?')
            
    elif choice == 3:
        son_name = input('What is the name of the son you want to add? ')
        son_name = son_name.title()
        if son_name in son_dict:
            print(son_name,'is already in the list, why don\'t you update it?')
        else:
            dad_name = input('Okay, and what is the father\'s name? ')
            grandad_name = input('Awesome, and what is the grandfather\'s name? ')
            son_dict[son_name] = (dad_name.title(),grandad_name.title())
            print('\nThanks you')
            
    elif choice == 4:
        son_name = input('What is the name of the son you want to update? ')
        son_name = son_name.title()
        if son_name in son_dict:
            dad_name = input('Okay, and what is the new father\'s name? ')
            son_dict[son_name] = dad_name.title()
            print('\nUpdated!')
        else:
            print(son_name,'isn\'t in the list, why don\'t you add it?')
            
    elif choice == 5:
        son_name = input('What is the name of the son you wish to remove? ')
        son_name = son_name.title()
        if son_name in son_dict:
            del son_dict[son_name]
            print('\nThanks,',son_name,'has been removed')
        else:
            print('Sorry, that name isn\'t in my list')
    else:
        print('Sorry, that isn\'t a valid choice')

        
input('\nPress enter to exit')
