#이것이 코딩 테스트다
#dfs(depth-first search) 깊이 우선 탐색
#스택(선입후출) 이용
#음료수 얼려 먹기

#틀린 부분 : dfs 응용하는 부분 -> 함수 들어가기 전에 배열 적용
#틀린 부분 : dfs 앞에 return 안해도 됨. 
def dfs(i,j) :
    if i>=0 and j>=0 and i<n and j<m :
        if graph[i][j] == 0 :
            graph[i][j] = 1
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1,)
            return True
    return False

n,m = map(int, input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

count = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True :
            count += 1
print(count)
