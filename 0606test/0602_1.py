#백준
#DFS BFS

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
li = []
for line in range(m) :
    line = tuple(map(int, sys.stdin.readline().split()))
    li.append(line)
li.sort()
graph = {}
for l in li :
    if l[0] not in graph :
        graph[l[0]] = [l[1]]
    else :
        graph[l[0]].extend([l[1]])
        graph[l[0]].sort()
    
    if l[1] not in graph :
        graph[l[1]] = [l[0]]
    else :
        graph[l[1]].extend([l[0]])
        graph[l[1]].sort()




print(graph)
def dfs(graph, start, visit = []) :
    visit = visit + [start]
    for node in graph[start] : 
        if node not in visit :
            visit = dfs(graph, node, visit)
    return visit

def bfs(graph, start) :
    visit = []
    queue = deque([start])
    while(queue) :
        node = queue.popleft()
        if node not in visit :
            visit.append(node)
            queue.extend(graph[node])
    return visit

print(*dfs(graph,v), sep = ' ')
print(*bfs(graph,v), sep = ' ')