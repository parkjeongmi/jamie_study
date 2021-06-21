#프로그래머스
#스택/큐
#기능개발
from collections import deque
import math
progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    todo = deque()
    for i in range(len(progresses)) :
        todo.append(math.ceil((100-progresses[i])/speeds[i]))
    answer = []
    while todo :
        count = 1
        now = todo.popleft()
        while len(todo)>0 :
            if todo[0] <= now :
                todo.popleft()
                count += 1
            else : break
        answer.append(count)
    return answer