from time import localtime
year = localtime().tm_year
year = int(year)
print("What is your name?")
fname = input()
print("What is your surname?")
sname = input()
print("Hello,",fname,sname,)
print("Your initials are",fname[0],sname[0])
print("What is your favourite hobby?")
hobby = input()
print("Wow! I like",hobby,"too!")
print("What team do you support")
team = input()
if team != "liverpool":
    print("nahh man they're shite. I support liverpool.")
else:
    print("Yesssss thennnnnnn")
print("What is your favourite game?")
game = input()
print("Yes! I love that game!")
print("Which year were you born in?")
yob = int(input())
print("Have you already had your birthday this year?")
bday = input()
if bday != "no" :
    age = year - yob
else:
    age = (year - 1) - yob
print("You are",age,"years old.")
if age < 18 :
    print("You are underage.")
if age > 17 :
    print("You are not underage.")
print("What is your favorite food?")
food = input().lower()
if food == "pizza":
    print("Same! I love pizza!")
else:
    print("Mmmm,",food,"is so yummy! I personally prefer pizza")
print("Where do you live?")
live = input()
print("That's a nice place! I live in a computer at judgemeadow.")
print("I would now like you to take the time to think about how sad your life is.")
print("You just spent the last two minutes having an entertaining coversation with a few lines of code.")
input()
