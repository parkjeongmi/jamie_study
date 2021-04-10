#이것이 코딩 테스트다
#bfs(breadth-first search) 깊이 우선 탐색
#큐(선입선출) 이용 / 최단 거리 이용
#특정 거리의 도시 찾기

#내가 풀었다!!!!!!1
#해결하지 못한 점 : list 형식의 리턴 값을 출력하는 법을 모르겠다 -> 일단 함수 밖에서 출력함
#시간초과
from collections import deque

def bfs(n,m,k,x,graph) :
    queue = deque([x])
    visited = [0] * (n+1)
    count = [0] * (n+1)
    while queue :
        now = queue.popleft()
        for i in graph :
            if i[0] == now and visited[i[1]] == 0 :
                queue.append(i[1])
                count[i[1]] = count[i[0]] + 1
                visited[i[1]] = 1
    answer = []
    for i in range(n) :
        if count[i+1] == k :
            answer.append(i+1) 
    return answer

n,m,k,x = map(int, input().split())
graph = []
for i in range(m) :
    graph.append(list(map(int, input().split())))
if len(bfs(n,m,k,x,graph)) == 0 : print(-1)
else :
    for i in bfs(n,m,k,x,graph) : print(i)