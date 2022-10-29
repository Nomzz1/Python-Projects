def collatz(n):
    if n % 2 == 0:
        return n / 2
    if n % 2 == 1:
        return 3 * n + 1
values = [32, 5, 16, 8, 4, 2, 1]
chain = []
def isLoop(n):
    if n in chain:
        print(chain)
        return False
    if n in values:
        return True
    else:
        chain.append(n)
        x = collatz(n)
        return isLoop(x)
num = 1
while True:
    if isLoop(num) == True:
        num += 1
    else:
        break

