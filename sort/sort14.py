#프로그래머스
#정렬
#가장 큰 수

#목표 : 순서 재배치해 가장 큰 수 문자열로 return
#알고리즘 1. 배열을 가장 크게 만드는 원소 선택하기
#알고리즘 2. 해당 원소를 배열에 붙이기
#알고리즘 3. 전체 배열 출력하기

numbers = [6,1,2]

def solution(numbers):
    s_numbers = [str(x) for x in numbers]
    s_numbers.sort(key = lambda x : (x*4)[:4], reverse=True)
    if s_numbers[0] == '0' : return("0")
    else : return("".join(s_numbers))

list = [1,2,3,4,5]
print(list[:3])