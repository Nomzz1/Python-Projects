print("Differentiation")
print("***************\n")
terms = int(input("How many terms of x are there in your equation?\n"))
equation = ""
def diff(x, y):
    x *= y
    y -= 1
    global equation
    if x < 0:
        if y == 1:
            equation = equation + str(x) + "x "
        elif y == 0:
            equation = equation + str(x) + " "
        else:
            equation = equation + str(x) + "x^" + str(y) + " "
    if coeff > 0:
        if y == 1:
            equation = equation + "+ " + str(x) + "x "
        elif y == 0:
            equation = equation + "+ " + str(x) + " "
        else:
            equation = equation + "+ " + str(x) + "x^" + str(y) + " "
for i in range(1, (terms+1)):
    print("\nFor term number",i,"in your equation:")
    coeff = int(input("What is the coefficient value of x?\n"))
    while coeff == 0:
        print("That is not a valid value.")
        coeff = int(input("What is the coefficient value of x?\n"))
    power = int(input("What is the power value of x?\n"))
    diff(coeff, power)
if equation[0] == "+":
    length = len(equation)
    equation_new = equation[1:length]
    print("Your differentiated equation is:",equation_new)
else:
    print("Your differentiated equation is:",equation)