#프로그래머스
#다리를 지나는 트럭
from collections import deque
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
#index = [0,0,0,0]
#index는 bridge_length 증가하는 거 체크
#index = [0 * i  for i in range(len(truck_weights))]
truck_weights = deque(truck_weights)
going = deque()
index = deque()
answer = 0
check = 0
while True :
    if check == 1 :
        index.popleft()
        going.popleft()
    if len(truck_weights) > 0 and (sum(going) + truck_weights[0]) <= weight :
        now = truck_weights.popleft()
        going.append(now)
        index.append(0)
    answer+=1
    check = 0
    if len(index) > 0 :
        for i in range(len(index)) :
            index[i] += 1
            if index[i] == bridge_length :
                check = 1
    if len(going) == 0 and len(truck_weights) == 0 :
        break
print(answer)



