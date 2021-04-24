#프로그래머스
#heap
#디스크 컨트롤러

#목표 : 각 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리할 경우 평균
#알고리즘1. len(list)==0이면 먼저 요청이 들어온 작업부터 처리
#알고리즘2. len(list)>0 이면 작업시간이 작은 것부터 처리
import heapq

jobs = [[0,3],[1,9],[2,6]]
import heapq
def solution(jobs):
    jobs.sort()
    count = 0
    last = -1
    time = jobs[0][0]
    wait = []
    length = len(jobs)
    answer = 0
    while (count <length) :
        for s, t in jobs :
            if last < s <= time :
                heapq.heappush(wait, (t,s))
        if len(wait) > 0  :
            last = time
            term, start = heapq.heappop(wait)
            count+=1
            time += term
            answer += (time-start)
        else : time+=1
    return answer//length


# work = []
# jobs.sort(key=lambda x : x[0])
# heapq.heapify(jobs)
# heapq.heapify(work)
# sum = []
# while True :
#     if len(jobs) == 0 :
#         break
#     now = heapq.heappop(jobs)
#     if len(work) == 0 :
#         heapq.heappush(work, now)
#     if work[0][0]  < now[0] :
#         now[0] += now[0] - work[0]
#         sum.append(heapq.heappop(work))
# list_sum = [sum(x) for x in work]
# print(list_sum)