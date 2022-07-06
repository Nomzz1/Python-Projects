import time
print("Welcome to the chatterbox!")
print("**************************\n")
print("Choose a colour (Red, Green, Blue or Yellow):")
colour = input().lower()
if colour == "red":
    print("R")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    print("D")
    time.sleep(0.5)
    numset = "(3, 4, 5 or 6):"
elif colour == "yellow":
    print("Y")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    print("L")
    time.sleep(0.5)
    print("L")
    time.sleep(0.5)
    print("O")
    time.sleep(0.5)
    print("W")
    time.sleep(0.5)
    numset = "(3, 4, 5 or 6):"
elif colour == "blue":
    print("B")
    time.sleep(0.5)
    print("L")
    time.sleep(0.5)
    print("U")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    numset = "(1, 2, 7 or 8):"
elif colour == "green":
    print("G")
    time.sleep(0.5)
    print("R")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    print("N")
    time.sleep(0.5)
    numset = "(1, 2, 7 or 8):"
else:
    print("That is not a valid colour.")
    print("Restart the Program")
    input()
print("Choose a number",numset)
num = int(input())
num %= 2
if num == 1:
    if numset == "(3, 4, 5 or 6):":
        numset = "(1, 2, 7 or 8):"
    elif numset == "(1, 2, 7 or 8):":
        numset = "(3, 4, 5 or 6):"
print("Choose a number",numset)
num = int(input())
if num == 1 or num == 2:
    print("TRUTH: Who do you like?")
if num == 3 or num == 4:
    print("TRUTH: List 5 reasons why you are my friend.")
if num == 5 or num == 6:
    print("DARE: Chug a can whole of soda.")
if num == 7 or num == 8:
    print("DARE: Go in the shower fully clothed.")
