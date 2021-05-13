#프로그래머스
#DFS, BFS
#여행 경로

#방문하는 공항 경로를 배열에 담아 Return
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets) :
    #한 노드에서 갈 수 있는 경로를 routes에 dictionary로 표현
    #key에 t[0]가 있으면 있는 값에 t[1] 더한 리스트, 없으면 [] + t[1] 
    #routes = {"ICN" : ["SFO", "ATL"], "SFO" : ["ATL"], "ATL" : ["ICN", SFO"]}
    routes = {}
    for t in tickets :
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    #routes의 value들을 알파벳 역순으로 정렬
    for r in routes :
        routes[r].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    while len(stack) > 0 :
        top = stack[-1]
        #routes에 다음 값이 없으면 -> pop해서 path에 넣기
        if (top not in routes) or len(routes[top]) == 0 :
            path.append(stack.pop())
        #routes 값이 있으면, stack에 넣기
        else :
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]
print(solution(tickets))