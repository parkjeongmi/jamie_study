#이것이 코딩 테스트다
#bfs(breadth-first search) 깊이 우선 탐색
#큐(선입선출) 이용 / 최단 거리 이용
#특정 거리의 도시 찾기

#나랑 다른 점 : 나는 그대로 graph에 입력 받아서 비교할게 많음 -> 시간 초과
#나랑 다른 점 : graph[노드 번호] -> 연결된 노드 // 입력받을 때부터 정돈함 => 시간 충족
#나랑 다른 점 : 출력 시, if에 하나라도 해당하면 check=True로 바뀌고, False일 경우 분리시킴


from collections import deque
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
count = [-1] * (n+1)
count[x] = 0
while queue :
    now = queue.popleft()
    for i in graph[now] :
        if count[i] == -1 :
            count[i] = count[now] + 1
            queue.append(i)

check = False
for i in range(n) :
    if count[i+1] == k :
        print(i+1)
        check = True
if check == False:
    print(-1)
