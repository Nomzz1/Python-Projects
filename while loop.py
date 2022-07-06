print("Add the Number Game!")
print("********************\n")
print("Enter numbers to add together the press 0 to exit.")
count = 0
running_total = 0
number = int(input("Input the first number: "))

while number != 0:
    count = count + 1
    running_total = running_total + number
    number = int(input("Input next number: "))
print("You entered",count," numbers")
print("Total =",running_total,)
input()
