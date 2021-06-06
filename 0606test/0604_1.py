#백준
#미로탐색
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range(n)]
count_graph = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = [[0,0]]
count_graph[0][0] = 1
while queue :
    y, x = queue.pop(0)
    if x == m ad y == n :
        break
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n :
            if graph[ny][nx] == 1 and not visit[ny][nx] :
                visit[ny][nx] = True
                queue.append([ny,nx])
                count_graph[ny][nx] += count_graph[y][x] + 1
print(count_graph[n-1][m-1])
