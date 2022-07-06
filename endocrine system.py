from time import sleep
import random
print("Welcome to the Endocrine System Simulator!")
print("******************************************\n")
sleep(1)
print("This program simulates the homeostasis of blood glucose level.")
print("Let's begin!\n")
sleep(1)
print("You are a human. You have a standard BGC of 5.0")
print("Your goal throughout this game is to keep that as level as possible.")
bgc = 5.0
sleep(1)
print("\n You will be given a choice of 4 actions to do.")
print("You must choose the correct actions to keep your BGC level.")
sleep(1)
print("At any time, input 0 to exit the game.")
def main():
    sleep(1)
    print("Choose your next action:")
    print("1: Exercise")
    print("2: Eat")
    print("3: Do nothing")
    print("4: Sleep")
    choice = int(input())
    if choice == 0:
        pass
    elif choice == 1:
        exercise()
    elif choice == 2:
        eat()
    elif choice == 3:
        nothing()
    elif choice == 4:
        Sleep()
    else:
        print("That is not a valid choice, please type 1, 2, 3 or 4.")
def check():
    if bgc == 0:
        print("Oh no! Your BGC has reached 0!\n")
        print("That is too low!")
        gameover = " G A M E   O V E R "
        for i in gameover:
            print("\r",i, sep = "")
            sleep(0.2)
    elif bgc == 10:
        print("Oh no! Your BGC has reached 10!\n")
        print("That is too high!")
        gameover = " G A M E   O V E R "
        for i in gameover:
            print("\r",i, sep = "")
            sleep(0.2)
    elif bgc < 5.0:
        print("Careful! Your BGC is lower than standard!")
        print("Now you have to do something to bring it up.")
        main()
    elif bgc > 5.0:
        print("Careful! Your BGC is higher than standard!")
        print("Now you have to do something to bring it down.")
        main()
def exercise():
    time = random.randint(1,4)
    print("You exercised for",time,"hours.")
    reduce = time/2.2
    print("This reduced your BGC by",reduce,"units.")
    global bgc
    bgc -= reduce
    sleep(1)
    check()
def eat():
    cal = random.randint(100,600)
    print("You ate a meal worth",cal,"calories.")
    increase = cal/220
    print("This increased your BGC by",increase,"units.")
    global bgc
    bgc += increase
    sleep(1)
    check()
def nothing():
    time = random.randint(1,4)
    print("You did nothing for",time,"hours.")
    
