#이것이 코딩 테스트다
#그리디
#거스름돈

n = 1260

def solution(n) :
    coin = [500,100,50,10]
    result = 0
    for i in coin :
        result += n//i
        n%=i
    return print(result)

solution(n