#!/usr/bin/env python
def traverse(path, M, T, opt, N):
        p = path[-1]
        if T[p] != -1:
                pathsum = sum(M[i] for i in path) + T[p] - M[p]
                if pathsum < opt:
                                opt = pathsum
                                return T[p]
        if sum([M[i] for i in path]) > opt: return False
        if (p+1)%N != 0:
                path.append(p+1)
                tmp = traverse(path,M,T,opt,N)
                path.pop()
                if T[p]==-1: T[p]=tmp+M[p]
                elif T[p] > tmp+M[p]: T[p]=tmp+M[p]
        if len(M)-1-p >= N:
                path.append(p+N)
                tmp = traverse(path,M,T,opt,N)
                path.pop()
                if T[p]==-1: T[p]= tmp+M[p]
                elif T[p] > tmp+M[p]: T[p]=tmp+M[p]
        return T[p]

N = 80
M = []

file = open("test1.txt")
#for line in file: print line


for line in file:
        M = M + [int(x) for x in line.strip().split(",")]

print M
# T = [-1 for x in range(len(M))]
# T[-1] = M[-1]
# opt = sum(M)
# path = [0]
# print traverse(path,M,T,opt,N)
