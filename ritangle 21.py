def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def rootSum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

def productSum(n):
    total = 1
    for i in str(n):
        total *= int(i)
    return total

primes = []
for i in range(2,1000000):
    if isPrime(i):
        primes.append(i)

def apointer(n):
    if isPrime(n):
        try:
            if (rootSum(n) + n) == primes[primes.index(n)+1]:
                return True
        except IndexError:
            return False
    return False

def ampointer(n):
    if isPrime(n):
        try:
            if (rootSum(n) + productSum(n) + n) == primes[primes.index(n)+1]:
                return True
        except IndexError:
            return False
    return False

for i in primes:
    if (not apointer(i)) and ampointer(i):
        print(i)
        break
