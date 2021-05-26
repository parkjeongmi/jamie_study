#스택/큐
#프로그래머스
#프린터

priorities = [3,3,3,1]
location = 3

from collections import deque

pri = deque()
pri.extend(priorities)
go = []

#중요도에 따라 정렬하는 알고리즘
#현재 위치를 찾는 알고리즘

while len(pri) > 0 :
    now = pri.popleft()
    if pri :
        if max(pri) > now :
            pri.append(now)
        else : 
            go.append(now)
            if location == 0 :
                break
    else :
        go.append(now)
        break
    if location == 0 :
            location = len(pri)-1
    else :
        location -= 1

print(len(go))





