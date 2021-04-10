#이것이 코딩 테스트다
#다이나믹 알고리즘 : 주어진 공간을 효율적으로 사용하는 알고리즘
#최적 부분 구조 (탑다운) : 재귀함수를 이용해 큰 문제를 작은 문제로 분해하여 해결하는 하향식 알고리즘
#중복 부분 구조 (바텀업) : 반복문을 이용해 작은 문제를 반복해 해결하는 상향식 알고리즘

#효율적인 화폐 구성
#모르겠음

def solution(n,m,money) :
    how[0] = 0
    for i in range(n) :
        for j in range(money[i], m+1) :
            if how[j-money[i]] != 10001 :
                how[j] = min(how[j], how[j-money[i]]+1)
    if how[m] == 10001 :
        return -1
    else : return how[m]

money = []
n, m = map(int, input().split())
how = [10001] * (m+1)
for i in range(n) :
    money.append(int(input()))

print(solution(n,m,money))


