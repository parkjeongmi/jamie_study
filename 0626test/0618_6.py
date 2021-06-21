#구현
#별찍기6

n = int(input())
for i in range(n-1,-1,-1) :
    star= 2*i+1
    null_left = (2*n-1-star)//2
    print(" "*null_left+"*"*star)