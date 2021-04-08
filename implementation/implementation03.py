#이것이 코딩 테스트다
#구현
#왕실의 나이트
#틀린 부분 : 이동 경우수를 리스트 형식으로 미리 넣어야 하는데, dx dy로 나타냄
#틀린 부분 : 아스키코드 고려해서 숫자로 변환하는 과정 = a를 ord로 변환하고 96빼기

data = input()

def solution(data) :
    column = int(ord(data[0])-96)
    row = int(data[1])
    count = 0

    move_type = [[-2, 1],[2,1],[-2,-1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    
    for i in move_type : 
        next_row = row + i[0]
        next_column = column + i[1]
        if next_row >0 and next_column > 0 and next_row<9 and next_column<9 : 
            count+=1
    return count
print(solution(data))