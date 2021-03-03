#프로그래머스
#스택,큐
#기능개발
import math
def solution(progresses, speeds) :
    stack = []
    answer = []
    days = 0
    for i in range(len(progresses)) :
        days = math.ceil((100-progresses[i])/speeds[i])

        if i == 0 :
            stack.append(days)
        else : 
            if stack[0] >= days :
                stack.append(days)
            else :
                answer.append(len(stack))
                stack.clear()
                stack.append(days)
    answer.append(len(stack))
    return answer
