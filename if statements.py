#Worksheet 1
#Challenge 1
age = int(input("How old are you?\n"))
if age < 18:
    print("You cannot vote")
if age >= 18:
    print("You can vote.")
    
#Challenge 2
password =  input("Enter the password: ")
if password == "Letmein":
    print("Access granted.")
    
#Challenge 3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
ans = (num1 + num2)/2
if ans < 100:
    print("The average is", ans)
print("Goodbye.")

#Worksheet 2
#Challenge 1
pizza = input("Do you like pizza?\n").lower()
if pizza == "yes":
    print("I like pizza too!")
else:
    print("My favourite food is pizza.")
    
#Challenge 2
password =  input("Enter the password: ")
if password == "Letmein":
    print("Access granted.")
else:
    print("Access denied.")
    
#Challenge 3
num = int(input("Enter a number: "))
if num > 100:
    print("Thank you")
else:
    num += 100
    print("I have changed it as your number is too low.")
print("Your number is",num)
