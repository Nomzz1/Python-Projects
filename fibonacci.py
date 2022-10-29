from time import sleep
basenum = int(input("Base number: "))
loop = 0
num = basenum
addnum = basenum
print(basenum)
while loop != 1:
    oldnum = num
    num += addnum
    addnum = oldnum
    print(num)
    sleep(0.005)
