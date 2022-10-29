from math import ceil
print("Welcome to the uber price calculator.")
miles = float(input("How many miles? "))
time = input("What is the time (e.g. '7:30')? ")
ampm = input("AM or PM? ").lower()
cancel = input("Is the ride cancelled? ").lower()
wait = int(input("How long is the wait (in seconds)? "))
baseCharge = 7.00
charge = baseCharge + miles * 0.2
time = time.split(":")
if ((7 <= int(time[0]) <= 9) and (ampm == "am")) or ((5 <= int(time[0]) <= 7) and (ampm == "pm")):
    charge *= 2
if cancel == "yes":
    charge += 4
charge += ceil(wait/30) * 0.4
print(f"Your ride will cost £{charge:.2f}")
