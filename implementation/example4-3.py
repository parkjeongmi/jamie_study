#이것이 코딩 테스트다
#구현
#왕실의 나이트

a = input()

def solution(a) :
    row = int(a[1])
    column = int(ord(a[0]))-int(ord('a'))+1
    steps = [(-2,1), (-2,-1), (2, 1), (2,-1), (1,2),(-1,2), (1,-2),(-1,-2)]

    result = 0
    for step in steps :
        next_row = step[1] + row
        next_column = step[0] + column
        if next_row > 0 and next_row <=8 and next_column > 0 and next_column <= 8 :
            result +=1
    return print(result)

solution(a)

