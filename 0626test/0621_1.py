#프로그래머스
#스택/큐

from collections import deque
def solution(priorities, location):
    d = deque([(v, i) for i,v in enumerate(priorities)])
    answer = 0
    while len(d) :
        now = d.popleft()
        if d and max(d)[0] > now[0] :
            d.append(now)
        else :
            answer +=1
            if now[1] == location :
                break
    return answer