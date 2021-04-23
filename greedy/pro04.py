#프로그래머스
#그리디
#구명보트

#목표 : 모든 사람을 구출하기 위해 필요한 구명보트 최솟값
#알고리즘1. people 돌면서 리스트에 넣기 
#알고리즘2. 현 원소 + list 원소 <= 100 : pop하고 answer+=1
#알고리즘2-2. list 원소를 다 확인해야하는데..=> 이중포문은 비효율적임
#만약 두 원소 합이 <100라면, list에 넣기

#알고리즘3. people 다 돌았지만 리스트 길이>0이면, 길이만큼 answer 더하기



people = [70,50,80,50]
limit = 100

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people)-1
    while(start<end) :
        if people[start]+people[end] <= limit :
            answer +=1
            end -= 1
        else :
            answer+=1
        start+=1
    if start==end : answer+=1
    return answer




# for p in (people) :
#     if len(list)==0 : list.append(p)
#     else :
#         if p + list.pop() <= 100 :
#             answer+=1
#         else : list.append(p)
# if len(list)>0 :
#     answer+=len(list)
# print(list)