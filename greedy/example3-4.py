#이것이 코딩 테스트다
#그리디
#1이 될 때까지

n, k = map(int, input().split())

def solution(n, k) :
    count = 0
    #이 조건 잊지 말기!
    while(n>=k) :
        while (n%k != 0) :
            n = n-1
            count+=1
        n /= k
        count+=1
    while(n>1) :
        n-=1
        count+=1
    return count
print(solution(n,k))
    


    