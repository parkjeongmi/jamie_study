#프로그래머스
#스택큐
#다리를 지나는 트럭

#트럭이 다리를 지나가는데 걸리는 최소 시간 : 큐(대기행렬)
#return : 모든 트럭이 다리를 건너는데 걸리는 최소 시간
#bridge_length (1초에 1씩 가는 트럭이 움직여야하는 길이)
#weight : 다리가 버틸 수 있는 무게 (truck_weights의 합이 초과하면 안됨)
#truck_weights : 지나가야하는 각 트럭의 무게

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge_ing = deque()
    weight_sum = 0
    count = 0
    for i in range(bridge_length) :
        count+=1
        for truck in truck_weights :
            if (sum <= weight)
                bridge_ing.append(truck) 
                sum+=truck
        if 
            
    return count