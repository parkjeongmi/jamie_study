#구현
#별찍기5

#출력형식이 다르다는 오류 발생 = 뒷부분에는 공백 두는 거 아님

n = int(input())

for i in range(0,n) :
    star= 2*i+1
    null_left = (2*n-1-star)//2
    print(" "*null_left+"*"*star)

