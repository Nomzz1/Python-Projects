import random
def rnp():
    name = input("Enter a name: ")
    names.append(name)
print("Welcome to the Random Name picker!")
print("How many names would you like to enter?")
t = int(input())
names = []
for value in range(t):
    rnp()
choice = random.choice(names)
print("The name chosen is:",choice+"!")
