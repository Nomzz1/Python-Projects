import random
repeat = True
score = 0
while repeat == True:
    print("Press enter to roll the dice.")
    input()
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print("You rolled a",die1,"and a "+str(die2)+".")
    if die1 == die2:
        print("This is a double, so your score is 0")
        score = 0
        repeat = False
    else:
        print(die1+die2,"will be added to your score.")
        score += die1 + die2
        error = True
        while error == True:
            print("Would you like to go again?")
            check = input().lower()
            if check == "yes":
                repeat = True
                error = False
            elif check == "no":
                repeat = False
                error = False
            else:
                print("That is not a valid answer.")
                error = True
print("Your score is "+str(score)+".")
print("Goodbye.")
