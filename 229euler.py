#!/usr/bin/env python
import math

LIMIT = 1e7

mex = int(LIMIT**0.5)
bmex2 = int((LIMIT/2)**0.5)
bmex3 = int((LIMIT/3)**0.5)
bmex4 = int((LIMIT/7)**0.5)

def C1(mex, LIMIT):
    s1 = set([a*a+b*b for a in range(1,mex) for b in range(1,a+1) if a*a+b*b <= LIMIT])
    return s1

def C2(mex, bmex2, LIMIT, s):
    s2 = set([a*a + 2*b*b for a in range(1,mex) for b in range(1,bmex2+1) if a*a+2*b*b in s])
    return s2

def C3(mex, bmex3, LIMIT, s):
    s3 = set([a*a + 3*b*b for a in range(1,mex) for b in range(1, bmex3+1) if a*a+3*b*b in s ])
    return s3

def C4(mex, bmex4, LIMIT, s):
    s4 = set([a*a + 7*b*b for a in range(1,mex) for b in range(1, bmex4+1) if a*a+7*b*b in s ])
    return s4


s = C1(mex, LIMIT)
s = C2(mex, bmex2, LIMIT, s)
s = C3(mex, bmex3, LIMIT, s)
s = C4(mex, bmex4, LIMIT, s)

print "There are " + str(len(s)) + " such numbers that do not exceed " + str(LIMIT) + ".\n"


