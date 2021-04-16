#프로그래머스
#힙
#더 맵게 

#목표 : 스코빌 지수 K 이상
#알고리즘1. 가장 맵지 않은 음식의 스코빌 지수 + 두 번쨰로 맵지 않은 음식의 스코빌 지수 *2
#알고리즘2. 모든 음식의 스코빌 지수가 K 이상일 때까지 반복
#알고리즘3. K의 최소 횟수 return (불가면 -1)

#heap 활용
#1. heapq.heappush(heap, item) -> 추가 
#2. heapq.heappop(heap) -> 최소 값 제거
#3. heapq.heapify(x) -> 변경

import heapq
scoville = [1,2,3,9,10,12]
K = 7

def solution(scoville, K) :
    i = 0
    count = 0
    len_s = len(scoville)
    while True : 
        change = 0
        for i in scoville :
            if i < K :
                change = 1
        if change == 1 :
            s=[]
            s.append(heapq.heappop(scoville))
            s.append(heapq.heappop(scoville)*2)
            heapq.heappush(scoville, sum(s))                
            count+=1  
        else : break 
    if count == 0 : return -1        
    return count
print(solution(scoville,K))