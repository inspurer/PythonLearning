# -*- coding:utf-8 -*-
# Filename: DirectedGraph.py
# --------------------
# Function description:path searching of directed graph
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-16, Updated on 2015-12-17
# --------------------
def searchPath(graph, start, end):
    results = []
    __generatePath(graph, [start], end, results)
    results.sort(key = lambda x:len(x))
    return results

def __generatePath(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                #path.append(n)
                __generatePath(graph, path + [n], end, results)
def showPath(results):
    print('The path from ',results[0][0], ' to ', results[0][-1], ' is:')
    for path in results:
        print(path)
if __name__ == '__main__':
    graph = {'A':['B', 'C', 'D'],
             'B':['E'],
             'C':['D', 'F'],
             'D':['B', 'E', 'G'],
             'E':['D'],
             'F':['D', 'G'],
             'G':['E']}
    r1 = searchPath(graph, 'A', 'D')
    showPath(r1)
    r2 = searchPath(graph, 'A', 'E')
    showPath(r2)
