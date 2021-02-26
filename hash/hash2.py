#프로그래머스
#해시
#전화번호 목록

#리스트의 원소가, 다른 원소에 포함될 경우 판별

#zip 함수 활용
def solution(phoneBook) :
    phoneBook = sorted(phoneBook)
    
    for i, j in zip(phoneBook, phoneBook[1:]) :
        if j.startswitch(i) : return False
    return True

#hash 활용
def solution(phoneBook) :
    answer = True
    hash_map = {}
    for i in phoneBook :
        hash_map[i] = 1
    for i in phoneBook :
        temp = ""
        for j in phoneBook :
            temp += j
            if temp in hash_map and temp != i :
                answer = False
    return answer

#추가
def solution(phoneBook) :
    for i in phoneBook :
        temp = ''
        for j in i :
            temp += j
            if temp in phoneBook and temp != i :
                return False
    return True