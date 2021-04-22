#프로그래머스
#그리디
#체육복

#알고리즘1. 모든 학생의 수로 배열을 초기화한다.
#알고리즘2. lost 해당 학생은 -1, reserve 해당 학생은 +1
#알고리즘3. 앞 학생이 0 현재가 2라면 앞에 빌려주기, 혹은 뒷 학생이 0 현재가 2라면 뒤에 빌려주기

n = 5
lost = [2,4]
reserve = [3]

#배열 존재 알고리즘
def solution(n, lost, reserve):
    s = [1] * (n+2)
    for i in lost :
        s[i] -= 1
    for i in reserve :
        s[i] += 1
    for i in range(1, n+1) :
        if s[i] == 2 and s[i-1] == 0 :
            s[i-1:i+1] = [1,1]
        elif s[i]==2 and s[i+1] == 0 :
            s[i:i+2] = [1,1]
    return len([x for x in s[1:-1] if x > 0])

#집합 함수 활용 알고리즘
s = set(lost) & set(reserve)
l = set(lost) - s
r = set(reserve) - s
#s는 잃어버리고 가져온 학생 교집합
#l은 잃어버리고 안가져온 학생 -> 빌려야 하는 학생
#r은 가져와서 안빌려준 학생 -> 빌려줄 수 있는 학생

#l의 원소 꺼내서 -> l-1이 r에 있으면 제거, l+1이 r에 있으면 제거
#n에서 l 원소 수 빼기

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    
    for i in sorted(r) :
        if i-1 in l :
            l.remove(i-1)
        elif i+1 in l :
            l.remove(i+1)
    return n-len(l)

d = {1,2,3}
for i in list(d) :
    print(i)