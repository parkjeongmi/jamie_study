#이것이 코딩 테스트다
#최단 경로 알고리즘 : 최단 경로를 구하는 알고리즘
#다익스트라 알고리즘 : 특정 노드에서 다른 노드로 가는 최단 경로를 구하는 알고리즘

#우선순위 큐 : 우선순위가 높은 데이터를 가장 먼저 삭제하는 알고리즘
#힙 : 우선순위 큐를 구현하기 위한 알고리즘 (최소 힙, 최대 힙)

import heapq
def heapsort(iterable) :
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, value)
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

def heapsort_desc(iterable) :
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, -value)
    for i in range(len(h)) :
        result.append(-heapq.heappop(h))
    return result


result = heapsort_desc([1,3,5,7,9,2,4,6,8,0])
print(result)