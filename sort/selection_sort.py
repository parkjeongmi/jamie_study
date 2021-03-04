#선택정렬 : 매번 가장 작은/큰 것만 선택한다
#시간 복잡도 : O(n^2)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)) :
    min = i
    for j in range(i+1, len(array)) :
        if array[j] < array[min] :
            min = j
    array[i], array[min] = array[min], array[i]
print(array)