#프로그래머스
#정렬
#가장큰수

numbers = [0, 0, 0]

#1. numbers를 정렬한다
#lambda x는 str로 미리 바꿔서 넣어야 함
numbers = [str(x) for x in numbers]
numbers.sort(key=lambda x : [x*4][:4], reverse=True)

#2. 이어 붙여서 출력한다

print("".join(numbers))


def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x : [x*4][:4], reverse=True)
    if numbers[0] == '0':
        return "0"
    return "".join(numbers)