#프로그래머스
#전화번호목록

#sort로 정렬하니깐 -> p1과 p2 크기가 차이 날 수 밖에 없음
#배운점 1. zip 함수 활용
#배운점 2. startswith 함수 활용

phone_book = ["119", "97674223", "1195524421", "12345", "67899"]
phone_book.sort(reverse=True)
for p1, p2 in zip(phone_book, phone_book[1:]) :
    if p1.startswith(p2) :
        print("yes")