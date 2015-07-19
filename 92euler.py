#!/usr/bin/env python
#How many starting numbers below ten million will arrive at 89?
M = {}
M[1] = False
M[89] = True
Ans = 0
#Squares = [x**2 for x in range(1,10)]
def determine(M, n):
    if n < 1: return
    global Ans
    tmp = n
    chain = [tmp];
    while n not in M:
        #print "line 27: " + str(M) +"\t"+ str(chain)
        if tmp in M:
            for i in chain:
                M[i] = M[tmp]
            break
        tmp = sum([int(x)**2 for x in str(tmp)])
        chain.append(tmp)
    Ans += M[n]
    #print "line 34: " + str(M)+"\t"+ str(Ans)
    return M[n]

for n in range(1000000): determine(M, n)
print Ans
