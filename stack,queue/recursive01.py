#이것이 코딩 테스트다
#재귀함수
#팩토리얼 예제

#1. 반복문 이용한 팩토리얼
def factorial_iterative(n) :
    result = 1
    if n == 0 or n == 1 : 
        return 1
    else : 
        for i in range(n, 0, -1) :
            result *= i
        return result

#2. 재귀함수 이용한 팩토리얼
def factorial_recursive(n) :
    if n == 0 or n == 1 : 
        return 1
    else :
        return n * factorial_recursive(n-1)


print(factorial_recursive(5))
    