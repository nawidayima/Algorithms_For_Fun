#!/usr/bin/env python
import sys
NM = raw_input().split()
N = int(NM[0])
M = int(NM[1])
tuples = [raw_input().split() for x in range(N)]
K = int(raw_input().strip())
tuples.sort(key = lambda x: int(x[K]))
print '\n'.join([' '.join([e for e in t]) for t in tuples])
