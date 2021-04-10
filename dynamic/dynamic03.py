#이것이 코딩 테스트다
#다이나믹 프로그래밍 : 한정된 자료 공간을 가장 효율적으로 해결하는 알고리즘
#최적 부분 구조 (탑다운) : 재귀함수로 큰 문제를 작은 문제로 분해하여 해결하는 하향식 알고리즘
#중복 부분 구조 (바텀업) : 반복문으로 작은 문제를 반복해서 해결하는 상향식 알고리즘

#개미 전사
#틀린 부분 : d[0], d[1]은 먼저 넣고 시작하는 것
#틀린 부분 : d[i]는 이전 값과, 현 값+두번째 이전 값 중 큰 값을 고르는 로직
def solution(n, array) :
    d[0] = array[0]
    d[1] = max(d[0], array[1])

    for i in range(2, n) :
        d[i] = max(d[i-1], d[i-2]+array[i])
    return d[n-1]
        

n = int(input())
array = list(map(int, input().split()))
d = [0] * n
print(solution(n, array))