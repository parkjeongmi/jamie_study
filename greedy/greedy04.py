#이것이 코딩 테스트다
#그리디 : 기준에 따라 가장 좋은 것을 선택하는 알고리즘
#거스름돈


def change(money) :
    sum = 0
    using = [500,100,50,10]

    for i in using :
        if money == 0 : return sum
        coin = money // i
        money -= (i*coin)
        sum += coin
    return sum

money = int(input())
print(change(money))