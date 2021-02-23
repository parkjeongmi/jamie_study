#하루 자라는 양을 기준으로 오름차순 정렬 -> 작은 값부터 자르기
#1. grow 기준으로 오름차순 정렬
#2. grow[i] * (n-i) + height[i]


import sys
n = int(input())
tree = list(map(int, sys.stdin.readline().split()))
grow = list(map(int, sys.stdin.readline().split()))
sortedgrow = sorted(grow, reverse=False)
sum = 0
for i in range(n) :
    ms = sortedgrow[0]
    index = grow.index(ms)
    a = sortedgrow.index(ms)
    sum += ms*i+tree[index]
    del sortedgrow[a]
print(sum)