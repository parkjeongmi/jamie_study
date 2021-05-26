#스택/큐
#프로그래머스 
#주식가격

prices = 	[1,2,3,2,3,1]

from collections import deque
def solution(prices):
    
    list = deque()
    list.extend(prices)
    r_list = []
    while (len(list)>0) :
        target = list.popleft()
        r = 0
        for i in list :
            if target <= i :
                r += 1
            else :
                if r == 0 : 
                    r = 1
                    break
                else : 
                    r += 1
                    break
        r_list.append(r)
    
    return r_list

#알게된 점 : for문 안쓰고 바로 popleft()로 제거