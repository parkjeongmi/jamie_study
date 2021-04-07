#이것이 코딩 테스트다
#그리디 : 기준에 따라 가장 좋은 경우를 선택하는 알고리즘
#숫자 카드 게임
#틀린 부분 : list를 입력 받는 부분, map 함수를 이용할 경우 list로 형변환해줘야 함

select = []
n, m = map(int, input().split())
for i in range(n) : 
    data = list(map(int, input().split()))
    data.sort()
    select.append(data[0])
select.sort(reverse=True)
print(select[0])




