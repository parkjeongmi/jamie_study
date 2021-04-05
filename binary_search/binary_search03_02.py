#이것이 코딩 테스트다
#이진탐색
#부품 찾기
#계수정렬로 풀기

n = int(input())
array = [0] * 100001

for i in input().split() :
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for one in x : 
    if array[one] == 1 : 
        print("yes", end=' ')
    else : print("no", end = ' ')
