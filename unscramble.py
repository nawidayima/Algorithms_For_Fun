#!/usr/bin/env python
words = open('/usr/share/dict/words')

dictionary = {}
#create dictionary
for word in words:
    word = word.strip()
    if word not in dictionary:
        dictionary[word] = True

word = raw_input("please enter word to unjumble: " )

def permute(path, unvisited, dictionary, solution):
    if not len(unvisited):
        if path in dictionary:
            solution[path] = True
        return
    else:
        for i in range(len(unvisited)):
            path += unvisited[0]
            unvisited = unvisited[1:]
            permute(path,unvisited,dictionary, solution)
            unvisited += path[-1]
            path = path[:-1]

solution = {}
permute("", word, dictionary, solution)

print '/n'.join([k for k in solution])
