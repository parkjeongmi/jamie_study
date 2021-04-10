#이것이 코딩 테스트다
#다익스트라 프로그래밍 : 한정된 공간을 효율적으로 사용하는 알고리즘
#최적 부분 구조 (탑다운) : 재귀로 큰 문제를 작은 문제로 분해하여 하향식으로 해결하는 알고리즘
#중복 부분 문제 (바텀업) : 반복문으로 작은 문제를 반복해 상향식으로 해결하는 알고리즘 

#틀린 부분 1. 시작점 : (1,1)에서 시작하면 될 줄 알았는데, 1열부터 최대 값을 비교해서 정해야 함.
#틀린 부분 2. 값 비교 : 세 방향으로 이동했을 때의 값을 모두 max에 넣고 비교하기

t = int(input())
for i in range(t) :
    n, m = map(int, input().split())
    gold = []
    for i in range (n*m) :
        gold.append(input())
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

def book_solution(n,m,gold) :
    dp = []
    index = 0
    for i in range(n) :
        dp.append(gold[index:index+m])
        index += m
    
    for j in range(1, m) :
        for i in range(n) :
            if i == 0 :
                left_up = 0
            else : 
                left_up == dp[i-1][j-1]
        if i == n-1 :
            left_down = 0
        else : 
            left_down = dp[i+1][j-1]
        
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n) :
        result = max(result, dp[i][m-1])

