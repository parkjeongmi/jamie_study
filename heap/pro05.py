#프로그래머스
#heap
#더 맵게

scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K) :
    answer= 0
    heapq.heapify(scoville)
    while True :
        min1 = heapq.heappop(scoville)
        if min1 >= K : break
        elif len(scoville) == 0 :
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        now = min1+min2*2
        heapq.heappush(scoville, now)
        answer +=1
    return answer
        
print(solution(scoville, K))