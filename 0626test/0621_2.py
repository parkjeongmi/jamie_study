#프로그래머스
#스택/큐
#주식가격

from collections import deque
prices = 	[2, 4, 3, 1, 5]
#[1, 2, 3, 2, 3]

#stack 이용한 풀이 모르겠음
def stack_solution(prices) :
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices) :
    #(0,2), (1,4), (2,3), (3,1), (4,5)
        #stack이 비어있지 않고 & price가 stack의 첫번째 index의 price보다 작을 때
        while stack and price < prices[stack[-1]] :
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    while stack :
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer
    

def brute_force(prices) :
    answer = [0] * len(prices)
    for i in range(len(prices)) :
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                answer[i] += 1
            else :
                answer[i] += 1
                break
    return answer


#효율성 최악인 내 코드
def solution(prices):
    d = deque(prices)
    answer = []
    while len(d) :
        now = d.popleft()
        count = 1
        if len(d) > 1 :
            if (max(d) >= now) and (min(d) >= now) :
                count = len(d)
            else :
                for d_first in d :
                    if d_first >= now :
                        count += 1
                    elif (d_first < now) and count>1 :
                        break
                    else :
                        count = 1 
                        break
        elif len(d) == 1 :
            if d[0] >= now :
                count = 1
        else :
            count = 0
        answer.append(count)
    return answer
