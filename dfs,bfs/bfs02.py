#이것이 코딩 테스트다
#bfs(breadth-first searh) 깊이 우선 탐색
#큐(선입선출) 이용 / 최단 경로 찾을 때 이용
#미로 탈출

#틀린 부분 : bfs는 반복문 사용인데, 재귀 사용하려고 함
#틀린 부분 : dx, dy 이용하는게 익숙하지 않음.
#틀린 부분 : 최단 경로 찍을 시 count 따로 안만들고 graph[x][y]에 바로 1 더해서 계산
#틀린 부분 : 시작점이 (0,0)인데 (1,1)로 시작함

from collections import deque
def bfs(x, y) :
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m :
                if graph[nx][ny] == 1 :
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]
n,m = map(int, input().split())
graph =[]
for i in range(n) :
    graph.append(list(map(int, input())))

print(bfs(0,0))
