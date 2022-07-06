from webbrowser import open
def fun(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fun(n - 1) + fun(n - 2)
s = ""
for i in range(1,6):
    s += str(fun(i))
open(f"www.multisoft.se/{s}")