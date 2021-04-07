#이것이 코딩 테스트다
#그리디 : 기준에 따라 가장 좋은 것을 선택하는 알고리즘
#1이 될 때가지

def until_one(n, k) :
    count = 0
    while(n != 1) :
        if (n%k==0) :
            n /= k
            count += 1
        else :
            n -= 1
            count +=1
    return count

n, k = map(int, input().split())
print(until_one(n,k))