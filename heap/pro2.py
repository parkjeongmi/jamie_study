#프로그래머스
#힙
#디스크 컨트롤러

#작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리 -> 평균

import heapq
jobs=[[0,3],[1,9],[2,6]]

def solution(jobs) :
    #힙에 원소를 넣어서 대기 시간 비교하기
    #현재 시간 hour로 check
    #알고리즘1. heap이 비었을 때 -> 원소 하나 넣기 
    #알고리즘2. 새로운 원소가 들어오면, 해당 시점 부터 차례가 되어 나갈때까지 time 체크
    #알고리즘3. 원소 별 time의 평균 구하기
    #알고리금4. 이 전체 과정은 모두 진행해서 최소 값 구하기
    working = []
    time = []
    hour = 0
    i = 0
    while(True) :
        try : 
            now = jobs[i]
            if (now[0] == hour) and working == []:
                heapq.heappush(working,now[1])
            if hour == now[1] :
                heapq.heappop(working)
                heapq.heappush(time, hour-now[0])
            hour +=1 
            i += 1
        except IndexError : break
    answer = sum(time) // len(jobs)
    return answer

def solution_answer(jobs) :
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    while i < len(jobs) :
        for j in jobs :
            if start < j[0] <= now :
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0 :
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now-current[1])
            i+=1
        else : now +=1
    return int(answer/len(jobs))

print(solution_answer(jobs))
