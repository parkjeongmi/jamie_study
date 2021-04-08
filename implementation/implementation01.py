#이것이 코딩 테스트다
#구현
#시뮬레이션 : 명령에 따라서 개체를 차례대로 이동
#상하좌우
def solution(n, array) :
    x = 1
    y = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    type = ['U', 'D', 'L', 'R']
    for i in array :
        for j in range(len(type)) :
            if i==type[j] :
                x += dx[j]
                y += dy[j]
                if x <= 0 : x = 1
                elif y <= 0 : y = 1
    return y, x
n = int(input())
array = input().split()

answer = solution(n, array)
for i in answer :
    print(i, end=' ')