#스택/큐
#프로그래머스
#다리를 지나는 트럭


#sum 사용하면 시간초과남
from collections import  deque

bridge_length = 100
weight = 100
truck_weights = [10]

going = deque()
# for i in range(0, bridge_length) :
#     going.append(0)
going = deque([0 for _ in range(bridge_length)])
    
hour = 0
next = 0
going_weight = 0
while len(going) != 0 :
    hour+=1
    out = going.popleft()
    going_weight -= out
    if truck_weights :
        #truck_weights가 빈 리스트 방지하려면 위와 같이!
        if going_weight + truck_weights[0] <= weight :
            next = truck_weights.pop(0)
            going.append(next)
            going_weight += next
        else : going.append(0)

print(hour)
# while True :

#     if going_weight==0 and len(truck_weights)==0 :
#         break
#     if next == 0 and len(truck_weights) > 0 :
#         next = truck_weights.pop(0)
#         going_weight += next
#     hour+=1
#     out = going.popleft()
#     going_weight -= out
#     if going_weight + next <= weight :
#         going.append(next)
#         next= 0
#     else : going.append(0)
# print(hour)

