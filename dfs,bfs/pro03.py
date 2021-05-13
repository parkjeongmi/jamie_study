#프로그래머스
#DFS, BFS
#네트워크

#목표 : 네트워크 개수 구하기

n = 3
coumputers = [[1,1,0], [1,1,0],[0,0,1]]

def solution(n, computers) :
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n) :
        if visited[com] == False :
            #방문하지 않았을 경우 DFS
            DFS(n, computers, com, visited)
            answer += 1
    return answer
def DFS(n, computers, com, visited) :
    visited[com] = True
    for connect in range(n) :
        if connect != com and computers[com][connect] == 1 :
            if visited[connect] == False :
                DFS(n, computers, connect, visited)