#!/usr/bin/env python

def check(a,b):
#     a3 a2 a1
#        b2 b1 x
# ---------------
#  v4 v3 v2 v1
#  w4 w3 w2  0 +
#  --------------
#  y4 y3 y2 y1

#  c4 c3 c2 c1
    
    a1 = a%10
    a2 = (a/10)%10
    a3 = a/100
    b1 = b%10
    b2 = b/10
   
    v1 = (b1*a1)%10
    v2 = (b1*a2 + b1*a1/10)%10
    v3 = (b1*a3 + (b1*a2 + b1*a1/10)/10 )%10
    v4 = (b1*a3 + (b1*a2 + b1*a1/10)/10 )/10

    w2 = (b2*a1)%10
    w3 = (b2*a2 + b2*a1/10)%10
    w4 = (b2*a3 + (b2*a2 + b2*a1/10)/10 )%10
    w5 = (b2*a3 + (b2*a2 + b2*a1/10)/10 )/10
    if (w5):
        return ()

    y1 = v1
    y2 = (v2 + w2)%10
    y3 = (v3 + w3 + (v2 + w2)/10 )%10
    y4 = (v4 + w4 + (v3 + w3 + (v2 + w2)/10 )/10 )
    
    c1 = a1 + b1 + v1 + y1
    c2 = a2 + b2 + v2 + w2 + y2
    if (c2 != c1):
        return ()
    c3 = a3 + v3 + w3 + y3
    if (c3 != c2):
        return ()
    c4 = v4 + w4 + y4
    if (c4 != c3):
        return ()
    else:
        return c1

solutions = [(a,b,check(a,b)) for a in xrange(100,1000) for b in xrange(10,100) if check(a,b)]
print '\n'.join([str(x[0])+"*"+str(x[1])+" = "+str(x[0]*x[1])+", all columns adding up to "+str(x[2]) for x in solutions])

