#t = 테스트 케이스의 개수
#j = 사탕의 개수 n = 상자의 개수
#r = 세로 길이, c = 가로 길이
import sys
t = int(input())
for i in range(t) :
    sum = 0
    index=0
    list =[]
    j, n = map(int, sys.stdin.readline().split())
    for _ in range(n) : 
        r, n = map(int, sys.stdin.readline().split())
        list.append(r*n)
    list.sort(reverse=True)
    while(sum<j) :
        for a in list :
            sum+=a
            index+=1
            if (sum>=j) : break
    print(index)