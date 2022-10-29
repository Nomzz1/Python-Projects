def fact(n):
    if n < 2:
        return 1
    else:
        num = 1
        for i in range(n):
            num *= i+1
        return num
def isStrong(n):
    num = str(n)
    total = 0
    for i in num:
        total += fact(int(i))
    return n == total

def genStrong(n):
    count = n
    num = 1
    genlist = []
    while count != 0:
        if isStrong(num) == True:
            count -= 1
            genlist.append(num)
        num += 1
    return genlist

