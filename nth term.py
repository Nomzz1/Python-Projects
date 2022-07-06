print("Nth term finder.")
print("**")
print("\nEnter your the first two terms of your linear sequence:")
num1 = int(input("1st term:"))
num2 = int(input("2nd term:"))
new1 = num2 - num1
new2 = num1 - new1
equation = ""
if new2 < 0:
  equation = (str(new1)+"n"+str(new2))
if new2 > 0:
  equation = (str(new1)+"n+"+str(new2))
if new2 == 0:
  equation = (str(new1)+"n")
print("The nth term is:", equation)