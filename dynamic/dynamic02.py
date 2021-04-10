#이것이 코딩 테스트다
#다이나믹 프로그래밍 : 한정된 공간을 효율적으로 사용하는 알고리즘
#최적 부분 구조 (탑다운) : 큰 문제를 작은 문제로 분해하여 하향식으로 해결
#중복 부분 문제 (바텀업) : 작은 문제를 중복해서 상향식으로 해결

#1로 만들기
#틀린 부분 : for문으로 만들어서 조건을 충족해도 계속 for문 돌게 됨.
#틀린 부분 : 아예 틀림 / for문을 작은 수부터 돌려서 min값 찾는 구조 => 바텀업
def make_one(x, count) :
    while(x!=1) :
        devide = [5,3,2]
        check = False
        for i in devide :
            if x%i == 0 :
                x /= i
                count+=1
                check = True
        if check == False :
            x-=1
            count+=1
    return count

def final_solution(x) :
    d = [0] * 3000
    for i in range(2,x+1) :
        d[i] = d[i-1] + 1
        if i%2 == 0 :
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0 :
            d[i] = min(d[i], d[i//3]+1)
        if i%5 == 0 :
            d[i] = min(d[i], d[i//5]+1)
    return d[x]

x = int(input())
print(final_solution(x))