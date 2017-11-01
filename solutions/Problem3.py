import sympy

def primeFactors(n):
    factors = []
    primes = list(sympy.primerange(3,n/2))
    print("Primes Length: " + str(len(primes)))
    for f in primes:
        if(isFactor(n, f)):
            factors.append(f)
    return factors

def isFactor(n, factor):
    if (n%factor==0):
        return True
    return False


print(primeFactors(13195) == [5,7,13,29])