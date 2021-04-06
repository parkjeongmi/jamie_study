#이것이 코딩 테스트다
#정렬 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
#계수 정렬 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 (count 이용)

array = [1,3,2,4,5,6,2,3,4,1]

def count_sort(array) :
    count = [0] * (max(array)+1)

    for i in range(len(array)) :
        count[array[i]] += 1
    for i in range(len(count)) :
        for j in range(count[i]) :
            print(i, end=' ')
count_sort(array)