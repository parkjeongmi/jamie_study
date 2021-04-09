#이것이 코딩 테스트다
#queue : 은행과 같이 들어온 순서대로 처리하는 '선입선출' 구조

#틀린 부분 : from collections import deque
#틀린 부분 : dequeue -> 'deque'
#틀린 부분 : queue.reverse()는 바로 출력 못함. print는 따로 해야 함

from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
#3 7 1 4

queue.reverse()
print(queue)
#4 1 7 3