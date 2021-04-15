#프로그래머스
#그리디
#체육복 : 체육 수업을 들을 수 있는 학생의 최대값
#규칙1. 여벌 체육복이 있음 -> 다른 학생에게 빌려줄 수 있음
#규칙2. 여벌 체육복인 학생이 도난 가능 -> 못빌려줌
#규칙3. 왼쪽과 오른쪽 학생에게만 빌려줄 수 있음

#알고리즘 1. 전체 - 못듣는학생
#알고리즘 2. 여벌 체육복 가져온 학생 중 도난 당한 학생 제외하기
#알고리즘 3. 여벌 체육복 양쪽에 도난 당한 학생 확인 -> 있으면 두 개 리스트 다 제외
#알고리즘 4. 도난 당했지만, 리스트에 남아있는 학생 수 세기
#-> 시간 초과

#전체 학생의 수
n = 5
#체육복을 도난당한 학생들의 번호
lost = [2,4]
#여벌의 체육복 가져온 학생의 번호
reserve = [1,3,5]

def solution(n,lost,reserve) :

    #알고리즘 2. 여벌 체육복 가져온 학생 중 도난 당한 학생 제외하기
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if reserve[j] == lost[i] :
                del reserve[j]
                del lost[i]
    #체육 수업 들을 수 있는 학생 수

    student = ['O'] * (n+1)
    for i in lost :
        student[i] = 'X'
    for i in reserve :
        student[i] = '+'

    if (student[1] == 'X') and (student[2] == '+') :
        student[1] = 'O'
        student[2] = '-'
    if n > 3 :
        for i in range(2, n+1) :
            if (student[i] == 'X') and (student[i+1] == '+') :
                student[i] ='O'
                student[i+1] = '-'
    if (student[n] =='X') and (student[n-1] =='+' ):
        student[n] ='O'
        student[n-1] = '-'
    sum = 0
    for i in range(n+1) :
        if student[i] == 'X' :
            sum += 1
    return n - sum
print(solution(n,lost,reserve))

def answer_solution(n,lost,reserve) :
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    #lost와 reserve 모두 중복되는 값은 제거해야 함.
    #set_reserve = set(reserve) - set(lost)
    #set_lost = set(lost) - set(reserve)


    for r in _reserve :
        f = r - 1
        b = r + 1
        if f in _lost :
            _lost.remove(f)
        elif b in _lost :
            _lost.remove(b)
    return n - len(_lost)