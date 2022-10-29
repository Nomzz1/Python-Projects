def isHarshad(n):
    num = 0
    for i in str(n):
        num += int(i)
    return (n%num) == 0

def genHarshad(n):
    num = 1
    count = n
    while count != 0:
        if isHarshad(num):
            gennum = num
            count -= 1
        num += 1
    return gennum
print(genHarshad(int(input("Enter number: "))))
