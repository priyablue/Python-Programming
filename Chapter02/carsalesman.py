# this is a car salesman program
# it takes the users car budget and adds on
# all the hidden extras and gives the true cost
# of a car in that price range



print("\t\t\tWelcome to Skippy's Autos")
budget = int(input("\t\t\tHow much do you want to spend? "))

dealerFee = budget / 100 * 10
licenseFee = budget /100 * 7.5
destinationCharge = 100
sunroofFee = 150
dealerPrep = 75

carTotal = dealerFee + licenseFee + destinationCharge + sunroofFee + dealerPrep + budget

print("\n\nAs with all dodgy car dealers there are a few hidden fees." \
      "Here is the true cost of a car with your budget £", carTotal)


input("\n\nPress Enter to exit")
