#!/usr/bin/env python
N = 1e10
ex = 7830457
ans = 2
bits = [int(bit)==True for bit in bin(ex)[2:]]

for i in range(len(bits)):
    bits[len(bits)-1-i] = ans if bits[len(bits)-1-i] else 1
    ans = (ans*ans)%N

ans = reduce(lambda a,b: (a*b)%N, bits)
ans = (ans*28433 + 1)%N
print ans

