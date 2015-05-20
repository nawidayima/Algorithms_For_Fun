#!/usr/bin/env python
s = raw_input("Enter string: ")
size = len(s)
matrix = [[s[i:j] for j in range(1,size+1) if j > i] for i in range(size)]
print '\n'.join(['\n'.join(x) for x in matrix])


