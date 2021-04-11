#이것이 코딩 테스트다
#최단 경로 알고리즘 : 최단 경로를 구함
#다익스트라 알고리즘 : 특정 노드에서 다른 노드로 가는 최단 경로를 구함 (음의 간선이 없을 경우)
#Step1. 시작 노드를 설정함
#Step2. 최단 경로 테이블을 초기화함
#Step3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택함
#Step4. 해당 노드에서 특정 노드까지의 비용을 계산해 최단 경로 테이블을 업데이트 함


INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m) :
    a,b,c = map(int, input().split())
    graph[a] = graph.append((b,c))

#틀린 부분 : index 초기화 안함
#틀린 부분 : for문 범위는 1부터 n까지임
def min_node() :
    min = INF
    index = 1
    for i in range(1, n+1) :
        if distance[i] < min and visited[i] == False :
            min = distance[i]
            index = i
    return index

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    
    #첫번째 for문의 목적 : graph의 start 노드에 대해 연결된 노드와의 거리를 distance에 업데이트 함
    for j in graph[start] :
        distance[j[0]] = j[1]

    #두번째 for문의 목적 : 시작 노드를 제외한 모든 노드를 반복
    for i in range(n-1) :
        now = min_node()
        visited[now] = True
        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1) :
    if dijkstra[i] == INF :
        print("Infinity")
    else : print(dijkstra[i])



