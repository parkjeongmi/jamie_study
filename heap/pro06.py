#프로그래머스
#heap
#이중우선순위큐


operations = ["I 7","I 5","I -5","D -1"]
import heapq
def solution(operations):
    queue = []
    for operation in operations :
            oper, number = operation.split()
            if oper == 'I' :
                heapq.heappush(queue, int(number))
            else : 
                if len(queue) >0 :
                    if number == "1" : 
                        queue.pop(queue.index(heapq.nlargest(1,queue)[0]))
                    else : 
                        heapq.heappop(queue)

    if len(queue) == 0 : answer = [0,0]
    else : 
        answer = [heapq.nlargest(1,queue)[0], heapq.nsmallest(1,queue)[0]]
    return answer

print(solution(operations))