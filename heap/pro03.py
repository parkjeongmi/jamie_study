#프로그래머스
#heap
#더 맵게

#목표 : 스코빌 지수를 K 이상으로 만드는 최소 횟수를 return 하시오
#알고리즘1. 작은 수 + 작은 수 *2해서 넣기
#알고리즘2. 작은 수가 K 이상이면 종료
#알고리즘3. 리스트 다 돌았는데 작은 수가 K 보다 작으면 -1

scoville = [1,2,3,9,10,12]
K = 7

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True :
        min1 = heapq.heappop(scoville)
        if min1 >= K :
            break
        elif len(scoville) == 0 :
            answer = -1 
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
        answer+=1
    return answer