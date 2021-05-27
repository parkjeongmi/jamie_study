#해시
#프로그래머스
#전화번호 목록

phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        size = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:size] :
            return False
    
    return True