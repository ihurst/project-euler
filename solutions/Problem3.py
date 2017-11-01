import sympy

def primeFactors(n):
    factors = []
    primes = sympy.primerange(3, n/2)
    print("Prime Generator Ready...")
    for f in primes:

        while isFactor(n, f):
            factors.append(f)
            n = n/f

        if(n==1):
            return factors

    return factors

def isFactor(n, factor):
    if (n%factor==0):
        return True
    return False


print(primeFactors(13195) == [5,7,13,29])

print(primeFactors(600851475143))