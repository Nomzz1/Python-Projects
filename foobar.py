import time

start = time.time()
#Starting here to include generating the primes

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

listOfPrimes = genPrimes(10005)
stringOfPrimes = ""
for i in listOfPrimes:
    stringOfPrimes += str(i)

def solution(n):
    return stringOfPrimes[n:n+5]

for i in range(10000):
    solution(i)

print(str(time.time() - start) + "seconds")