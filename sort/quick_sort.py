#퀵정렬 : 기준 데이터 설정 -> 그 기준보다 큰 데이터와 작은 데이터의 위치 바꿈
#시간복잡도 : O(NlogN) 
##basic : 첫 번째 데이터를 기준 데이터(pivot)으로 설정

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
    if start >= end :
        return
    pivot = start
    left = start+1
    right = end
    while(left<=right) :
        while(left<=end and array[left] <= array[pivot]) :
            left+=1

        while(right>start and array[right] >= array[pivot]) :
            right -=1
        if (left>right) :
            array[right], array[pivot] = array[pivot], array[right]

        else :
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)