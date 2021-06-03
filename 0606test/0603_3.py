#백준
#미로탐색
from collections import deque
import sys
def dfs(graph,start) :
    stack = deque([start])
    visit = []
    while stack :
        node = stack.popleft()
        if node not in visit :
            visit.append(node)
            if node in graph :
                temp = list(set(graph[node]) - set(visit))
                temp.sort(reverse=True)
                visit += temp
    return visit

n, m = map(int, sys.stdin.readline().split())
row = [[]for _ in range(m)]

for _ in range(n) :
    