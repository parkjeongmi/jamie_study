#이것이 코딩 테스트다
#정렬
#두 배열의 원소 교체
#array_a는 가장 작은 수를 k 번 고르고, array_b는 가장 큰 수를 k번 고른다
#선택, 삽입, 퀵, 계수


def quick_asc(array) :
    if len(array)<=1 : 
        return array
    pivot = array[0]
    tale = array[1:]

    left = [x for x in tale if x <= pivot]
    right = [x for x in tale if x > pivot]
    return quick_asc(left) + [pivot] + quick_asc(right)

def quick_des(array) :
    if len(array)<=1 :
        return array
    pivot = array[0]
    tale = array[1:]

    left = [x for x in tale if x > pivot]
    right = [x for x in tale if x <= pivot]
    return quick_des(left) + [pivot] + quick_des(right)

n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

a = quick_asc(array_a)
b = quick_des(array_b)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else : break

print(sum(a))