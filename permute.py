#!/usr/bin/env python

def permute(path, unvisited):
    if not unvisited:
        print ' '.join([str(x) for x in path])
        return
    else:
        for i in range(len(unvisited)):
            path.append(unvisited[0])
            unvisited.pop(0)
            permute(path,unvisited)
            unvisited.append(path[-1])
            path.pop(-1)


path = []
unvisited = raw_input("list objects to permute: ").split()

permute(path,unvisited)
