#프로그래머스
#스택/큐

from collections import deque
priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = []
while priorities :
    #2. priorities를 선입선출
    now = priorities.pop(0)
    if location == 0 :
        location = len(priorities)
    else :
        location -= 1
    #3. pop보다 큰 값이 있으면 append
    if max(priorities) > now :
        priorities.append(now)   
    #3-2. 없으면 제거
    else :
        answer.append(now)
        #4. location == index 값이 제거되는 순서 출력
        if now == priorities[location] :
            print(len(answer))
            break



