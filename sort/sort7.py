#이것이 코딩 테스트다
#정렬 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
#선택정렬 : 데이터 중 가장 작은 값을 골라 맨 앞으로 나열하는 것 -> 오름차순 정렬

array = [3,2,4,5,1]

for i in range(len(array)) :
    min_index = i
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

for i in array :
    print(i, end=' ')
