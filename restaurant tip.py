bill = float(input("How much is the bill? "))
people = int(input("How many people would you like to split the bill between? "))
tip = int(input("What percentage tip would you like to leave? "))
amount = ((1 + (tip/100)) * bill) / people
print(f"Each person should pay £{amount:.2f}")