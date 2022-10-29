from random import randrange
board = [["-" for i in range(8)] for i in range(8)]
def boardPrint():
    for i in board:
        print(i)
    print()
print("Here is an 8 x 8 board")
boardPrint()
tanks = 0
while tanks != 10:
    coord1 = randrange(8)
    coord2 = randrange(8)
    if board[coord1][coord2] == "-":
        board[coord1][coord2] = "T"
        tanks += 1
print("The board has now been populated by 10 random tanks.")
print("You must guess a series of coordinates to try and destroy all the tanks.")
print("If you cannot do so within 50 turns, you lose the game.")
turns = 50
tanks = 10
found = 0
while turns != 0:
    print("Enter the x-coordinate for the place you want to attack. It must be a number between 1 and 8.")
    x = int(input())
    print("Enter the y-coordinate for the place you want to attack. It must be a number between 1 and 8.")
    y = int(input())
    if board[y-1][x-1] == "T":
        tanks -= 1
        found += 1
        if found == 1:
            print(f"Well done, you found {found} Tank, {tanks} more to go!")
        else:
            print(f"Well done, you found {found} Tanks, {tanks} more to go!")
        board[y-1][x-1] = "X"
    elif board[y-1][x-1] == "X":
        print("You've already attacked this spot. Try again.")
        print("You will not lose a turn for this.")
    else:
        print("There are no tanks in this spot. Try again.")
    turns -= 1
    print(f"You have {turns} turns left.")
