#백준
#최소 스패닝 트리

#모든 정점 연결 + 가중치의 합 최소

#Kruskal Algorithm
#1. 간선 정렬
#2. 간선이 잇는 두 정점의 root를 찾음
#3. 다르다면 하나의 root를 바꾸어 연결

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def make_union(parent, a, b) :
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a<b :
        parent[b] = a
    else :
        parent[a] = b
