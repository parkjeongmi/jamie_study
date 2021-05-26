#스택/큐
#프로그래머스
#다리를 지나는 트럭

from collections import  deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

going = deque()
for i in range(0, bridge_length) :
    going.append(0)

hour = 0
next = 0
while True :
    if next == 0 :  
        next = truck_weights.pop(0)
    hour += 1
    going.popleft()
    if sum(going) + next <= weight :
        going.append(next)
        next = 0
    else : going.append(0)

    
    print(going)

while sum(going) > 0 :
    going.popleft()
    hour+=1

