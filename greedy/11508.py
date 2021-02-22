number = int(input())
price=[]
for _ in range(number) :
    price.append(int(input()))

price.sort(reverse=True)
setsum = 0 
for i in range(number) :
#number = 5 -> i = 0,1,2,3,4
#number = 4 -> i = 0,1,2,3
#number = 3 -> i = 0,1,2
    if(i%3 != 2) :
        setsum += price[i]
        #[5,4,3,2,1]
        #price [0] = 5 / price [1] = 4 / price[3] = 2  / price[4] = 1
        
        #[4,3,2,1]
        #price [0] = 4 / price [1] = 3 / price[3] = 1
        
        #[4,3]
        #price[0] = 4 / price=[1] = 3
print(setsum)

# <3보다 작은 경우>
#case 2 : (3,4) -> 7
#case 1 : (3) ->3

#<3보다 큰 경우>
#<3보다 큰 경우> <3의 배수인 경우>
#case 3 : (3,3,3) ->6
#case 6 : (3,2,4)(2,2,2) -> 11

#<3보다 큰 경우> <3의 배수가 아닌 경우>
#case 4 : (3,3,3), (4) -> 10
#case 5 : (3,3,2), (2,5) ->13

#총 개수에서 가장 작은 수인지
#case 6 : (1,2,3), (4,5,6) -> 18
#case 6 : (6,4,5), (5,5,5) -> 11 10+ 10 = 21

#앞에서 부터 3개의 묶음인지
#case 6 : (1,2,3), (4,5,6) -> 16
#case 6 : (6,4,5), (5,5,5) -> 11 + 10 -> 21