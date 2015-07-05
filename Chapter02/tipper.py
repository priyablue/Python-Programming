# this program works out just how much to tip
# based on a percentage of the bill

print("Welcome to the Bill Tipper program.")

billTotal = int(input("\nHow much is your bill?" \
                      " Round up the nearest pound please. "))


fiftenTip = int(billTotal / 100 * 15)
twentyTip = int(billTotal / 100 * 15)

print("\nIf your bill total is £",billTotal,", a 15% tip would be £" \
       ,fiftenTip,"\nIn total this is £",billTotal + fiftenTip)

print("\nIf you're feeling generous then a 20% tip would be £" \
       ,twentyTip,"\nIn total this is £",billTotal + twentyTip)

input("\n\nPress Enter to exit.")
