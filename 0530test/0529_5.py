#프로그래머스
#여행경로

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

start = "ICN"
graph = {}
for t in tickets:
    graph[t[0]] = graph.get(t[0], []) + [t[1]]

for g in graph :
    graph[g].sort(reverse=True)

#graph = {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}

visit = []
stack = [start]
while stack :
    node = stack[-1]
    if node not in graph or len(graph[node]) == 0 :
        visit.append(stack.pop())
    else :
        stack.append(graph[node][-1])
        graph[node] = graph[node][:-1]
    
print(visit[::-1])

