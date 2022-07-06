from time import sleep
values = ["32","5","4","2","1","16","8"]
chain = []
num = 24
def func(x):
    rem = x%2
    if rem == 0:
        y = x/2
    else:
        y = (3*x)+1
    print(int(x))
    if str(int(y)) in values:
        global num
        num += 1
        y = num
        print("\n")
    func(y)
func(num)