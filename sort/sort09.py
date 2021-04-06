#이것이 코딩 테스트다
#정렬 : 데이터를 특정한 기준으로 나열하는 것
#퀵정렬 : 특정한 원소를 기준으로 큰값과 작은 값을 찾아내 두 위치를 바꾸는 것

#틀린 부분 : 부등호 포함되는 부분 잘 봐야함.

array = [3,2,4,6,1,5]

def quick_sort(array, start, end) :
    if start >= end : 
        return
    pivot = start
    left = start+1
    right = end

    while (left <= right) :
        while (left <= end) and array[left] <= array[pivot] :
            left += 1
        while (right > start) and array[right] > array[pivot] :
            right -= 1 
        
        if (left > right) : 
            array[pivot], array[right] = array[right], array[pivot]

        else : array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

#틀린 부분 : array 길이가 1 이하면, array를 return
#틀린 부분 : [pivot] -> 정수는 배열 안에 넣어서 반환해야함
def quick_sort_python(array) :
    if len(array) <= 1 : return array

    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

quick_sort(array, 0, len(array)-1)
print(quick_sort_python(array))

#print (array)