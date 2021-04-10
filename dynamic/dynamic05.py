#이것이 코딩 테스트다
#다익스트라 프로그래밍 : 한정된 공간을 효율적으로 사용하는 알고리즘
#최적 부분 구조 (탑다운) : 재귀로 큰 문제를 작은 문제로 분해하여 하향식으로 해결하는 알고리즘
#중복 부분 문제 (바텀업) : 반복문으로 작은 문제를 반복해 상향식으로 해결하는 알고리즘 

t = int(input())
for i in range(t) :
    n, m = map(int, input().split())
    gold = []
    for i in range (n*m) :
        gold.append(int(input()))
    print(solution(n,m,gold))

def solution(n,m,gold) :
    x = 1
    y = 1
    catch = [0] * m
    moves = [[1,0],[1,-1],[1,1]]
    for i in range(m) :
        for move in moves :
            if x > 0 and y > 0 and x < n+1 and y < m+1 :
                x = x + move[0]
                y = y + move[1]
                now = (x-1)*4+y
                catch[i] = max(gold[now], catch[i])
    return sum(catch)

