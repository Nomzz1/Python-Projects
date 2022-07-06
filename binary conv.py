num1 = input("Enter a binary number to be converted: ")
den1 = 0
for digit in num1:
    den1 = den1*2 + int(digit)
print(den1)
