#구현
#별찍기8

n = int(input())

for i in range(1,n+1) :
    null = (n-i)*2
    print("*"*i+" "*null+"*"*i)
for i in range(n-1,0,-1) :
    null = (n-i)*2
    print("*"*i+" "*null+"*"*i)