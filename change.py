#Clay Kynor
#9/7/17
#change.py calculates change

cents = int(input("Input a number of cents: "))
quarters = (cents//25)
dimes = ((cents-(quarters*25))//10)
nickels = ((cents-(quarters*25)-(dimes*10))//5)
pennies = (cents-(quarters*25)-(dimes*10))-(nickels*5)
print("Quarters:",quarters)
print("Dimes:",dimes)
print("Nickels:",nickels)
print("Pennies:",pennies)