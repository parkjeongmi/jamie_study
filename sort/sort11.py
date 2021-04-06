#이것이 코딩테스트다
#정렬
#위에서 아래로 (내림차순)
#선택(x) 삽입 퀵(o) 계수(x)

def quick_sort(array) :
    if len(array)<=1 : return array
    pivot = array[0]
    tale = array[1:]
    left_side = [x for x in tale if x > pivot]
    right_side = [x for x in tale if x <= pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array=[]
n = int(input())
for i in range(n) : array.append(int(input()))

for i in quick_sort(array) : print(i, end=' ')