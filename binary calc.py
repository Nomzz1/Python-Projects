print("Enter the first binary number:")
num1 = input()
den1 = 0
for digit in num1:
    den1 = den1*2 + int(digit)
print("Enter the second binary number:")
num2 = input()
den2 = 0
for digit in num2:
    den2 = den2*2 + int(digit)
print("Enter the function:")
func = input()
if func == "-":
    answer = den1 - den2
elif func == "+":
    answer = den1 + den2
elif func == "*":
    answer = den1 * den2
elif func == "/":
    answer = den1 / den2
binans = bin(answer)
binans = binans.replace("0b","")
print("Your answer in binary is:",binans)
print("Your answer in denary is:",answer)