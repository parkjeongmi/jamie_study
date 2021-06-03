#백준 1260
#DFS BFS
#dict를 이용한 풀이

import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    if start not in graph :
        graph[start] = [end]
    elif end not in graph[start] :
        graph[start].append(end)
    if end not in graph :
        graph[end] = [start]
    elif start not in graph[end] :
        graph[end].append(start)

def dfs(graph, start) :
    stack = [start]
    visit = []
    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            if node in graph :
                temp = list(set(graph[node])-set(visit))
                temp.sort(reverse=True)
                stack += temp
    return visit

def bfs(graph, start) :
    queue = deque([start])
    visit = []
    while queue :
        node = queue.popleft()
        if node not in visit :
            visit.append(node)
            if node in graph :
                temp = list(set(graph[node]) - set(visit))
                temp.sort()
                queue += temp
    return visit


print(*dfs(graph,v), sep = ' ')
print(*bfs(graph,v), sep = ' ')

