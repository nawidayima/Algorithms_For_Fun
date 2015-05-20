#!/usr/bin/env python
import math

for n in xrange(10000):  
#    print "n = " + str(n)
    sum = 1
    for d in xrange(2,1+int(math.floor(n**0.5))):
 #       print " d = " + str(d)
        if n%d == 0:
  #          print "     " + str(n) + " is divisable by " + str(d)
            if n**0.5 == d:
                sum = sum + d
            else:
                sum = sum + d + n/d
   #         print "     sum is now: " + str(sum)
    if sum == n:
        print str(n) + " IS A PERFECT NUMBER!!"
   # print "\n"

