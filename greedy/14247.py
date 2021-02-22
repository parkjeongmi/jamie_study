#하루 자라는 양을 기준으로 오름차순 정렬 -> 작은 값부터 자르기
#1. grow 기준으로 오름차순 정렬
#2. grow[i] * (n-i) + height[i]

import sys
n = int(input())
#나무의 길이
height = [int(n) for n in input().split()]
#자라는 길이
grow = [int(n) for n in input().split()]
sum = 0
for i in range(n) :
    a = grow.index(max(grow))
    print(a)
    sum+= (max(grow) * (n-i) + height[a])
    del grow[i]
    height[a]
print(sum)


for i in range(n) :
    sum += height[i].first + grow.second* i



    # sum = 0
    # day = []
    # for i in range(5) :
    #     for j in range(5) : 
    #         day.append(height[j]+(grow[j]*(i+1)))
    #     sum+=max(day)
    #     #고른 인덱스를 자란 길이로 업데이트 하기
    #     new_index = day.index(max(day))
    #     new = grow[new_index]
    #     del height[new_index]
    #     height.insert(new_index, new)
    #     day = []
    # print(sum)


# day : 1+2*5 / 3+7*5 / 2+3*5 / 4+4*5 / 6+1*5
# 11 / 38 / 17 / 24 / 11
#day : 



