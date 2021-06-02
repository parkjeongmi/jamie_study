#백준
#DFS BFS

import sys

n, m, v = map(int, sys.stdin.readline().split())
li = []
for line in range(m) :
    line = tuple(map(int, sys.stdin.readline().split()))
    li.append(line)

#[(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]

def dfs(m, li, visit = []) :
    start = m 
    visit = visit + [start]

    
