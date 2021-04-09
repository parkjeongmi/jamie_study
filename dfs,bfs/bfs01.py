#이것이 코딩 테스트다
#bfs(breadth-first search) 너비 우선 탐색
#큐(선입선출) 이용 / 최단경로 찾을 때 이용

#틀린 부분 : bfs는 재귀함수를 이용하지 않음. while문을 이용해 queue안에 원소가 없을 때 까지 반복함!
from collections import deque

def bfs(graph,v,visited) :
    queue = deque([v])
    visited[v] = True
    while queue :
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now] :
            if visited[i] == False :
                queue.append(i)
                visited[i] = True




graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False]*len(graph)
bfs(graph, 1, visited)