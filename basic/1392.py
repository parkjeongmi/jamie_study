import sys
#n = 악보의 수
#q = 질문의 개수
n,q = map(int, sys.stdin.readline().split())

#n개의 악보가 차지하는 시간
n_hour = [int(sys.stdin.readline()) for _ in range(n)]
#알고자 하는 q개의 시간
q_hour = [int(sys.stdin.readline()) for _ in range(q)]

#출력 : q에 해당하는 악보의 번호
sum = []
time = 1
for i in n_hour :
    for _ in range(i) :
        sum.append(time)
    time+=1
for time in q_hour :
    print(sum[time])
