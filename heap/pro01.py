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

#시간초과 & 효율성 테스트
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

#알고리즘1. scoville 원소 하나씩 검소해서 K와 비교
#알고리즘1-2. K보다 작을 경우 -> 원소 두개 꺼내서 스코빌 변경
#문제. for문으로 검사하면 업데이트 반영 불가
def solution_second(scoville, K) :
    count = 0
    while True : 
        min = heapq.heappop(scoville)
        if min < K :
            heapq.heappush(scoville,min + (heapq.heappop(scoville) * 2))
            count += 1
        elif (min >= K) and (count > 0) : return count
        elif (min >= K) and (count ==0) : return -1
        else : continue

def solution_second(scoville, K) :
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K : 
        try :
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville) * 2)
            count += 1        
        except IndexError : return -1
    return count


#알고리즘1. scoville의 값을 다른 배열 h에 넣음
#알고리즘2. h의 최소값 두 개를 pop해서 h에 넣음 -> 계산 -> h에 다시 push
#알고리즘3. h[0]이 k보다 작을 때 진행

#알게된 점. 배열 길이 벗어나는 경우 -> try/except IndexError : return -1
#q. h를 왜 만들지?scoville에 바로 하면 되는거 아님? =? scoville은 heappush로 넣은게 아님! 즉 정렬되어 있지 않음
def solution_answer(scoville, K) :
    answer = 0
    h = []
    for i in scoville : 
        heapq.heappush(h, i)
    while h[0] < K :
        try :
            heapq.heappush(h, heapq.heappop(h)+heapq.heappop(h)*2)
        except IndexError : return -1
        answer += 1
    return answer

print(solution_second(scoville, K))  