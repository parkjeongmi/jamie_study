#이진탐색_반복문 (재귀 대신 while문)
#틀린 부분 : array[mid] 값과 비교해서 end, start 조절하는 부분

def binary_search(array, target, start, end) :
    while (start <= end) :
        mid = (start+end)//2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1 
        else : 
            start = mid + 1


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1) 
if result == None :
    print("없음")
else : print(result+1)


#10 7
# 1 3 5 7 9 11 13 15 17 19