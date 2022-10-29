values = []
def isHappy(n):
    if n == 1:
        values.clear()
        return True
    elif n in values:
        values.clear()
        return False
    else:
        values.append(n)
        x = sum([int(i)**2 for i in str(n)])
        return isHappy(x)
def genHappy(n):
    count = n
    num = 1
    genlist = []
    while count != 0:
        if isHappy(num):
            genlist.append(num)
            count -= 1
        num += 1
    return genlist
gen = int(input("How many happy numbers would you like to generate? "))
print(f"The first {gen} happy numbers are {genHappy(gen)}")
