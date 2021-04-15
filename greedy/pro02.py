#프로그래머스
#그리디
#조이스틱 : 조작 횟수의 최솟값을 return
#규칙1. 조이스틱의 방향은 네 가지다
#규칙2. 조작 횟수의 최소값을 return 해야한다.

#알고리즘1. A와 현 글자와의 차이 구하기 : ord('i') - ord('A') (A가 65니깐)
#알고리즘2. 차이가 13보다 클 경우, 반대로 움직임 -> 차이에서 13을 뺌
#=> A에서 계산한 값과 반대로 계산한 값 중 작은 값 고르기
#알고리즘3. name의 원소를 하나씩 돌아야함

#Q1. string을 처리하는 법 -> 문자열 인덱싱 가능 / len 확인도 가능
#Q2. 아스키코드 숫자로 변환하는 법 -> 문자를 아스키코드로 변환은 ord()
name = "JEROEN"
name2 = "JAN"

def solution(name) :
    count = 0
    for i in range(len(name)) :
        index = min((int(ord(name[i]))- int(ord('A'))), (int(ord('Z')- int(ord(name[i])))))
        if index == 0 : 
            count += 1
        else : 
            count+=index
            if i != len(name) :
                count+=1
    return count


def solution_answer(name) :
    #make_name은 변환할 최소값이 담긴 list
    make_name = [min(ord(i) - ord("A"), ord('Z') - ord(i) + 1) for i in name]

    idx, answer = 0, 0
    while True :
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0 :
            break

        #좌우 이동방향 정하기
        left, right = 1, 1
        while make_name[idx-left] == 0 :
            left += 1
        while make_name[idx+right] == 0 :
            right += 1

        #해당 방향으로 위치 조절 (모든 리스트의 값이 0이 될 때까지)     
        answer += left if left < right else right
        idx += -left if left< right else right
    return answer
print(solution_answer(name2))