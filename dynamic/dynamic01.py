#이것이 코딩 테스트다
#다이나믹 프로그래밍 : 한정된 공간을 효율적으로 해결하는 알고리즘
#최적 부분 구조 (탑다운) : 재귀함수를 이용하여 큰 문제를 작게 분해해 해결하는 하향식 알고리즘
#중복 부분 문제 (바텀업) : 반복문을 이용하여 작은 문제를 반복해 해결하는 상향식 알고리즘
#메모이제이션 : 이미 해결된 값을 저장해놓는 캐싱

#피보나치 수열 (단순 재귀)
def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    return fibo(x-1) + fibo(x-2)

#피보나치 수열 (메모이제이션)
def memoization_fibo(x) :
    if x == 1 or x == 2 :
        return 1
    if memo[x] != 0 :
        return memo[x]
    memo[x] = memoization_fibo(x-1) + memoization_fibo(x-2)
    return memo[x]

#피보나치 수열(보텀업)
def recursive_fibo(x) :
    re[1] = 1
    re[2] = 1
    for i in range(3, x+1) :
        re[i] = re[i-1] + re[i-2]
    return re[x]

x = 99
memo = [0] * (x+1)
re = [0] * (x+1)
print(recursive_fibo(99))