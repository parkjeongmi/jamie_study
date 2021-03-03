#프로그래머스
#큐,스택
#프린터

def solution(priorities, location):
    answer = 0
    from collections import deque
    d = deque([(v,i) for i,v in enumerate(priorities)])
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            #d를 앞에 왜 넣은지 모르겠음
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer