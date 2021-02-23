
import sys
n = int(input())
#나무의 길이
tree = [int(n) for n in input().split()]
#자라는 길이
grow = [int(n) for n in input().split()]


#하루 자라는 양을 기준으로 오름차순 정렬 -> 작은 값부터 자르기
#1. grow 기준으로 오름차순 정렬
#2. grow[i] * (n-i) + height[i]
sortedgrow = sorted(grow, reverse=True)
sum = 0
for i in range(5,0,-1) :
    index = grow.index(min(sortedgrow))
    sum += (min(sortedgrow) * i)+ tree[index]
    print(min(sortedgrow), index, tree[index], sum)
    del sortedgrow[index]
print(sum)

#1일차 : 1 제거 -> 6 + 1*5 =