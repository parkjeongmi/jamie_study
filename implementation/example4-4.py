#이것이 코딩 테스트다
#구현
#게임 개발
#실패

n, m = map(int, input().split())
a, b, d = map(int,input().split())

def solution(n,m,a,b,d) :
    array = []
    for i in range(n) :
        array.append(list(map(int, input().split())))

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    d = [[0]*m for _ in range(n)]
    d[a][b] = 1
    count = 1
    turn_time = 0
    while True :
        turn_left()
        nx = a + dx[d]
        ny = b + dy[d]
        if d[nx][ny] == 0 and array[nx][ny] == 0 :
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else : turn_time +=1
        if turn_time ==4 :
            nx = x - dx[d]
            ny = y - dy[d]
            if array[nx][ny] == 0 :
                x = nx
                y = ny
            else : break
            turn_time = 0
    return print(count)


def turn_left() :
    global d
    d -= 1
    if d == -1 :
        d = 3
    
solution(n,m,a,b,d)