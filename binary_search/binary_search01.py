#이진탐색 (재귀함수 이용)
#틀린 부분 : return 빼먹음 / mid 값 계산 틀림(start와 end를 더해야함)

def binary_search(array, target, start, end) :
    mid = (start+end) // 2
    if start > end : 
        return 0

    if array[mid] == target : 
        return mid
    elif array[mid] < target : 
        return binary_search(array, target, mid+1, end)
    else : 
        return binary_search(array, target, start, mid-1)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None :
    print("없음")
else : print(result+1)

#10 7
# 1 3 5 7 9 11 13 15 17 19