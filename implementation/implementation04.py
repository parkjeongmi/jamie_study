#이것이 코딩 테스트다
#구현
#시뮬레이션
#게임 개발
#문제 : 입력을 다 했는데 멈추지를 않음

def solution(n,m,x,y,direction,array) :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = [[0]*m for _ in range(n)]
    d[x][y] = 1
    count = 1
    turn_time = 0
    while True :
        #1. 현재 위치에서 왼쪽 방향부터 갈 곳 정하기
        direction -= 1
        if direction == -1 :
            direction = 3
        #2. nx, ny에 갈 좌표 찍음
        nx = x + dx[direction]
        ny = y + dy[direction]
        #2. 가보지 않은 칸이 존재하면 -> 전진
        if d[nx][ny]==0 and array[nx][ny]==0 :
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        #2. 가보지 않은 칸이 없다면 -> 회전
        else : turn_time += 1
        #3. 네 방향 모두 못가면 -> 한 칸 뒤로
        if turn_time == 4 :
            nx = x - dx[direction]
            ny = y - dy[direction]
            if array[nx][ny] == 0 :
                x = nx
                x = ny
            #3-2. 뒷 방향이 바다 -> 멈추기
            else :
                break
            turn_time = 0
    return count
    
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))
print(solution(n,m,x,y, direction, array))