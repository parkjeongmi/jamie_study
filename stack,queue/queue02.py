#프로그래머스
#큐스택
#주식가격

def solution(prices):
    #queue = prices
    queue = []
    for i in range(len(prices)) :
        count = []
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                count.append(prices[j])
            elif prices[i] > prices[j] :
                count.append(prices[j])
                break
        queue.append(len(count))
    return queue

#prices = [1,2,3,2,3]
prices = [1,2,3,2,3,1]
# prices[0] = 1 -> 5초
# prices[1] = 2 -> 4초
# prices[2] = 3 -> 1초
# prices[3] = 2 -> 2초
# prices[4] = 3 -> 1초
# prices[5] = 1 -> 0ch
# [5,4,1,2,1,0]

print(solution(prices))

#나랑 완전 반대로 풀었음 -> pop으로 첫번째 원소부터 빼서 for문과 비교 
# from collections import deque
# def solution_answer(prices):
#     answer = []
#     prices = deque(prices)
#     while prices:
#         c = prices.popleft()
#         count = 0
#         for i in prices:
#             if c > i:
#                 count += 1
#                 break
#             count += 1

#         answer.append(count)

#     return answer
