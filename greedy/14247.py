#하루 자라는 양을 기준으로 오름차순 정렬 -> 작은 값부터 자르기
#1. grow 기준으로 오름차순 정렬
#2. grow[i] * (n-i) + height[i]

import sys; input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))
grow.sort()
sum = 0
for index, value in enumerate(grow) :
    sum += tree[index] + value * index
print(sum)


#출력 초과
# import sys; input = sys.stdin.readline
# n = int(input())
# tree = [*map(int, input().split())]
# grow = [(x, i) for i, x in enumerate(map(int, input().split()))]
# grow.sort()
# r = 0
# for i in range(n) :
#     r += grow[i][0]*(i) + tree[grow[i][1]]
#     print(grow[i][0], i, grow[i][1], tree[grow[i][1]])
# print(r)


# 안되는 나의 코드
# import sys
# n = int(input())
# tree = list(map(int, sys.stdin.readline().split()))
# grow = list(map(int, sys.stdin.readline().split()))
# sortedgrow = sorted(grow, reverse=False)
# sum = 0
# for i in range(n) :
#     ms = sortedgrow[0]
#     index = grow.index(ms)
#     a = sortedgrow.index(ms)
#     sum += ms*i+tree[index]
#     del sortedgrow[a]
    
# print(sum)