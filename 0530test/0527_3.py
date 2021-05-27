#해시
#프로그래머스
#전화번호 목록

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        size = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:size] :
            return False
    
    return True

def solution(phone_book):
    phone_book.sort()
    dict = {}
    for phone in phone_book :
        if phone[0] not in dict.keys() :
            dict[phone[0]] = [phone]
        else :
            dict[phone[0]].extend([phone])
    for value in dict.values() :
        size = len(value)
        if size > 1 :
            for i in range(size-1) :
                if value[i] == value[i+1][:len(value[i])] :
                    return(False)
    return True
