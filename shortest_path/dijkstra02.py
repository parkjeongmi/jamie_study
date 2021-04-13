#이것이 코딩 테스트다
#최단 경로 알고리즘 : 최단 경로를 구함
#다익스트라 알고리즘 :특정 노드에서 다른 노드로 가는 최단 경로를 구함 (음의 간선일 떄 불가)
#우선순위 큐 이용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF : 
        print("INFINITY")
    else : print(distance[i])



