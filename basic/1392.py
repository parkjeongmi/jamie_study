import sys
n, q = map(int, sys.stdin.readline().split())

# n개의 악보가 차지하는 시간
n_akbo = [int(sys.stdin.readline()) for _ in range(n)]
# 알고자 하는 q개의 시간
q_hour = [int(sys.stdin.readline()) for _ in range(q)]

#출력 : q개의 시간에 해당하는 악보의 번호
arr = []
index = 1
for i in n_akbo : 
    #i = 2, 1, 3
    for j in range(i) :
        arr.append(index)
    index+=1
#arr = 1, 1, 2, 3, 3, 3

for k in q_hour :
    #k = 2, 3, 4, 0, 1
    
    print(arr[k])

# n_akbo = [2,1,3] -> 반복되는 횟수 
# q_hour = [2,3,4,0,1]
# 출력 -> [2,3,3,1,1]

# 시간별 출력되는 악보 : [1, 1, 2, 3, 3, 3]
# 출력해야 할 것 : 

# 2-> 2번째 원소의 값 => 2
# 3-> 3번째 원소의 값 => 3
# 4-> 4번재 원소의 값 => 3
# 0-> 0번째 원소의 값 => 1
# 1-> 1번째 원소의 값 => 1