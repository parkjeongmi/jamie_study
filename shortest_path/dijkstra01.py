#이것이 코딩 테스트다
#최단 경로 알고리즘 : 가장 짧은 경로를 찾는 알고리즘
#다익스트라 알고리즘 : 그래프에 여러 노드가 있을 때, 특정한 노드에서 다른 노드로 가는 각각의 최단 경로를 구함 (음의 간선이 없는 경우)

import sys
input = sys.stdin.readline()
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(n+1) :
    a,b,c = map(int, input().split())
    graph[a] = graph.append((b,c))

def min() :
    
