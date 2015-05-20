#!/usr/bin/env python
import math

def isqrt(x):
    if x < 0:
        raise ValueError('no real root')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def isPrime(n):
    return all(n%d!=0 for d in xrange(2,isqrt(n)+1))

primes = []

def sequence_found(primes):
    i = len(primes) - 1
    if i < 4:
        return []
    a = primes[i-5]
    b = primes[i-4]
    c = primes[i-3]
    d = primes[i-2]
    e = primes[i-1]
    f = primes[i]
    
    if (b==a+2)and(c==b+4)and(d==c+6)and(e==d+8)and(f==e+10):
        return [a, b, c, d, e, f]
    else:
        return []

for n in xrange(10000,100000):
    if isPrime(n):
        primes.append(n)
        check = sequence_found(primes)
        if (check):
            print '     '.join([str(x) for x in check])
            n = n + 5

