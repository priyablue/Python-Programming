# This program counts in increments set by the user


print('Welcome to the Counter Program')

start = int(input('\nWhere will I start counting from? '))
end = int(input('Where will I stop? '))
inc = int(input('How much should I count by?'))

print('\n\nThanks! Here goes...')

for i in range(start, end, inc):
    if (i % 41 == 0):
        print('BOOOOOBIESSSSS')
    else:
        print(i)


            
