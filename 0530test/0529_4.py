#BFS
#DFS

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

from collections import deque
def bfs(graph, start_node) :
    visit = []
    queue = deque(start_node)

    while queue :
        node = queue.popleft()
        if node not in visit :
            visit.append(node)
            queue.extend(graph[node])
    return visit


def dfs(graph, start_node, visit=[]) :
    visit = visit + [start_node]
    for node in graph[start_node] :
        if node not in visit :
            visit = dfs(graph, node, visit)
    return visit

def dfs_stack(graph,start_node) :
    stack = [start_node]
    visit = []
    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            if node in graph :
                temp = list(set(graph[node]) - set(visit))
                temp.sort(reverse=True)
                stack += temp
    return visit


print(bfs(graph, 'A'))
print(dfs(graph,'A'))
print(dfs_stack(graph,'A'))