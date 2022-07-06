piggybank = 0
while piggybank < 100:
    print("How much money do you want to put into the piggy bank?")
    money = float(input("£"))
    piggybank += money
    print("You currently have £"+str(piggybank)+" in your piggy bank.\n")
print("Well done!\nYou have reached your goal of £100!")
leftover = piggybank - 100
print("And you have £"+format(leftover, ".2f")+" leftover!")
