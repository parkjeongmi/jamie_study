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
print(solution(name2))
