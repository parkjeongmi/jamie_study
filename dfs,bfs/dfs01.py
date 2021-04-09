#이것이 코딩 테스트다
#dfs (depth-first search) 깊이 우선 탐색
#스택(선입후출)을 이용

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)



graph = [[], [2,3,8], [1,7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False]*len(graph)
dfs(graph,1,visited)