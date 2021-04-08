#이것이 코딩 테스트다
#구현
#시뮬레이션
#게임 개발

def solution(n,m,x,y,direction,array) :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = [[0]*m for _ in range(n)]
    d[x][y] = 1
    count = 1
    turn_time = 0
    while True :
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if d[nx][ny]==0 and array[nx][ny]==0 :
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else : turn_time += 1
        if turn_time == 4 :
            nx = x - dx[direction]
            ny = y - dy[direction]
            if array[nx][ny] == 0 :
                x = nx
                x = ny
            else :
                break
            turn_time = 0
    return count
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

print(solution(n,m,x,y,direction, array))