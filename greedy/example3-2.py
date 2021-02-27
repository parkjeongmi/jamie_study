#이것이 코딩 테스트다
#그리디
#큰 수의 법칙

import sys

n, m, k = map(int, input().split())
list = list(map(int, input().split()))

def solution(n,m,k,list) :
    list.sort()
    max_first = list[n-1]
    max_second = list[n-2]
    #가장 큰 수가 더해지는 횟수
    number = int(m/(k+1))*k+ m%(k+1)

    result = 0
    result += number*max_first
    result += (m-number)*max_second
    return print(result)

solution(n,m,k,list)