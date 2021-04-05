#이것이 코딩 테스트다
#이진탐색
#떡볶이 떡 만들기

#틀린 부분 : height 설정하는 위치가 while 문 안에 있어야 함

def binary_search(array, target, start, end) :
    result = 0
    while (start <= end) :
        height = (start+end) // 2
        sum = 0
        for i in array :
            if height < i :
                sum += (i-height)
        if sum < target :
            end -= 1
        elif sum >= target :
            result = height
            start += 1
    return result

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort()
result = print(binary_search(array, m, 0, max(array)))