#이것이 코딩 테스트다
#이진탐색
#부품 찾기
#set 함수로 풀기 : set함수는 집합 자료형을 초기화할 때 사용한다 => 데이터가 존재하는지 검사할 떄 효과적임

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in array : print('yes', end=' ')
    else : print('no', end=' ')