#이것이 코딩 테스트닫
#그리디 : 기준에 따라 가장 좋은 것을 선택하는 알고리즘
#큰 수의 법칙
#틀린 부분 : if 문과 대응하는 else 를 만들지 않았음

def bigger_number(m, k, array) :
    array.sort(reverse=True) 
    sum = 0
    count = 0
    for i in range(m) :
        if count == k : 
            sum += array[1]
            count = 0
        else : 
            sum += array[0]
            count += 1 
    return sum

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

print(bigger_number(m, k, array))
