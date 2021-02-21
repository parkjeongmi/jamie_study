#세개일 경우 -> 가장 작은 수는 제외한 총합
#세개가 아닌 경우 -> 총합

#입력 : 총 수 -> 가격
#출력 : 순서대로 세 묶음 -> 최소 비용

number = int(input())
price = []

#3개 중 최소 값 제외하고 더해주는 함수
def saleprice(list) :
    list.sort(reverse=False)
    del list[0]
    sum = 0
    for i in list :
        sum += i
    return sum

#가격 입력 받기
for _ in range(number) : 
    price.append(int(input()))

setsum = 0
#number = 1,2인 경우
if len(price) < 3 :
    for i in price :
        setsum+=i
else:
    #number = 3이상인 경우
    set = number//3
    rest = number%3
    for _ in range(set) :
        setsum+=saleprice(price[:3])
        del price[:3]        
    if rest > 0 :
        for i in price :
            setsum+=i
print(setsum)



#case : (3,3,3) (4) -> 10
#case : (3,2,1) (4) -> 9
#case : (3,3,3) (3,2) -> 11
#case : (3,3,3) (2,3,4) -> 13
#case : (2,4,3) (1,2) -> 10
#case : (2,1) ->3

#case 7 : (4,2,3), (2,4,3) ,(3) -> 7+7+3=17
#case 8 : (3,3,3),(3,3,3),(4,5)  -> 6 + 6+ 9 = 21