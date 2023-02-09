def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

def genPrimes(n):
    count = 0
    primeList = []
    while len(primeList) != n:
        if isPrime(count):
            primeList.append(count)
        count += 1
    return primeList

print(genPrimes(10_000))