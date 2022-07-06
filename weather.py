print("Where do you live?")
loc = input()
print("What's the weather like in",loc + "?")
weather = input()
if weather == "snowy" or weather == "cold":
    print("Mittens and earmuffs for you!")
elif weather == "sunny" or weather == "hot" or weather == "warm":
    print("Time for a picnic!")
elif weather == "rainy" or weather == "cloudy":
    print("Don't forget your umbrella!")
else:
    print("No particular advice.")
