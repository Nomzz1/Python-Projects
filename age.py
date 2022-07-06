def age_check(age):
    if age >= 16 and age <= 19:
        return True
    else:
        return False
age = int(input("Enter your age: "))
while age_check(age) == False:
    print("Age invalid")
    age = int(input("Enter your age: "))
print("Age valid")
