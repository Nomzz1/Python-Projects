PAYRATE = 10
MEAL = 15
UNIFORM = 5
print("What is the employee's name?")
name = input()
print("How many hours have they worked?")
hours = int(input())
gross = hours * PAYRATE
net = gross - (MEAL + UNIFORM)*2
print("Name:",name)
print("Hours Worked:",hours)
print("Gross Salary:",gross)
print("Deductions:",(MEAL + UNIFORM)*2)
print("Net Salary:",net)
input()