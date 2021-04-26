#프로그래머스
#dynamic
#n으로 표현

#목표 : N과 사칙연산만 사용해서 표현할 수 있는 방법 중 N 사용횟수의 최솟값 return

N = 5
number = 12
def solution(N, number):
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1) :
        x.add(int(str(N)*i))
    
    for i in range(len(s)):
        for j in range(i) :
            for op1 in s[j] :
                for op2 in s[i-j-1] :
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2!=0 :
                        s[i].add(op1//op2)
        if number in s[i] :
            answer = i+1
            break
        else : answer = -1
    return answer