#이것이 코딩 테스트다
#구현
#상하좌우

n = int(input())
plans = input().split()

def solution(n, plans) :
    x, y = 1, 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L', 'R', 'U', 'D']
    for plan in plans :
        for i in range(len(move_types)) : 
            if plan == move_types[i] :
                nx = x+dx[i]
                ny = y+dy[i]
        if nx < 1 or ny <1 or nx>n or ny>n :
            continue
        x, y = nx, ny
    return print(nx, ny)
solution(n, plans)

