#이것이 코딩 테스트다
#그리디
#숫자 카드 게임

import sys
n, m = map(int,input().split())
i = []
def solution(n, m) :
    card=[]
    result = 0
    for _ in range(n) :
        card = list(map(int, input().split()))
        min_value = min(card)     
        result = max(result, min_value)
    print(result)
solution(n,m)