#!/usr/bin/env python

# The prime 41, can be written as the sum of six consecutive primes:
# 
#     41 = 2 + 3 + 5 + 7 + 11 + 13
#     This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
#     The longest sum of consecutive primes below one-thousand that adds to a prime, 
#     contains 21 terms, and is equal to 953.
# 
#     Which prime, below one-million, can be written as the sum of the most consecutive primes?

LIMIT = 1000000

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

primes = [x for x in range(2,LIMIT) if isPrime(x)]

ans = []
for i in range(len(primes)):
    for j in range(i+1,len(primes)+1):
        c = primes[i:j]
        if sum(c) > LIMIT: break
        if isPrime(sum(c)) and len(c) > len(ans):
            ans = c

print str(sum(ans))#+" = "+' + '.join([str(x) for x in ans])
print "This is the sum of "+str(len(ans))+" consequetive primes and is less than "+str(LIMIT)

# print '\n'.join([str(x) for x in primes])


