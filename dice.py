import random
print("Press Enter to roll the die.")
roll = input()
while roll != "0":
    dice = random.randint(1, 6)
    print("You rolled a",dice)
    print("Press Enter to roll again or type 0 to exit.")
    roll = input()
print("Goodbye.")
input()
