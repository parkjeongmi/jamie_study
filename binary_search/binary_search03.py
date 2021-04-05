#이것이 코딩 테스트다
#이진탐색
#부품 찾기

#틀린 점 : Sort 안함!!!!!! 이진탐색의 핵심은 순서대로 방문!!!!!!

def binary_search(array, target, start, end) :
    mid = (start+end)//2
    if start > end : return None
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    else : return binary_search(array, target, mid+1, end)

def binary_search_while(array, target, start, end) :
    while (start <= end) :
        mid = (start+end)//2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid-1
        else : start = mid+1

n = 4
n_array = [4, 6, 3, 15]
m = 2
m_array = [3, 15]
print_result = []

n_array.sort()
m_array.sort()
for i in m_array :
    result = binary_search_while(n_array, i, 0, n-1)
    if result == None : print_result.append("no")
    else : print_result.append("yes")

for j in print_result :
    print(j, end=' ')
