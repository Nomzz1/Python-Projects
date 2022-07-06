import random
print("What is your favourite colour?")
colour = input() 
if colour == "red":
    power = "fire"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "green":
    power = "energy"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "blue":
    power = "lightning"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "black":
    power = "earth"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "white":
    power = "ice"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "orange":
    power = "amber"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "grey":
    power = random.choice(["speed","ash","metal"])
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "yellow":
    power = "sound"
    print("You are the",colour,"ninja")
    print("Your power is",power,)
elif colour == "purple":
    power = "evil"
    print("You are Garmadon")
    print("Your power is",power,)
elif colour == "brown":
    print("You are Darreth.")
    print("All hail Master Darreth.")
else:
    print("You are not a ninja.")
    print("You have no power.")
