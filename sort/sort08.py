#이것이 코딩 테스트다
#정렬 : 데이터를 특정한 기준에 따라 나열하는 것
#삽입 정렬 : 데이터를 적절한 위치에 삽입하는 것
 
array = [1,3,2,4,6,5]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else : break

for i in array : print(i, end=' ')