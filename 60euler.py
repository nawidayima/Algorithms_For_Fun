#!/usr/bin/env python

# The primes 3, 7, 109, and 673, are quite remarkable. 
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. 
#  The sum of these four primes, 792, represents 
#  the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which 
#  any two primes concatenate to produce another prime.

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
def nextPrime(n):
    ans = n + 1
    while (not isPrime(ans)): ans += 1
    return ans
def check(plist): #requires that plist contains only primes
    for i in range(len(plist)-1):
        for j in range(i+1, len(plist) ):
            a,b = str(plist[i]), str(plist[j])
            if not (isPrime(int(a+b)) and isPrime(int(b+a))): return ()
    return sum(plist)

plist = (2,3,5,7)
while not check(plist):



#print '\n'.join([str(x) for x in range(100) if isPrime(x)])
