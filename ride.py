print("Welcome to the ride!")
riders = 0
while riders < 8:
    print("This ride currently has",riders,"people on it.")
    print("How tall are you?")
    h = int(input())
    if h >= 140:
        print("You may enter the ride.")
        riders += 1
    elif h < 140 and h >= 120:
        print("Are you riding with an adult?")
        a = input()
        if a == "yes":
            if riders == 7:
                print("Sorry, the ride only has space for one more person.")
            else:
                print("You may enter the ride.")
                riders += 2
        if a == "no":
            print("You cannot enter the ride.")
            print("Sorry.")
    elif h < 120:
        print("You may not enter the ride.")
        print("Sorry.")
print("The ride is full.")
print("Sorry.")
