#문제 : 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻
# '(' 또는 ')'로 이루어진 문자열 s가 주어졌을 때, 올바른 괄호이면 true, 아니면 false

def solution(s) :
    if s[len(s)-1] == '(' :
    #전달받은 매개변수의 마지막 값이 '('인지 확인 -> 만약 맞다면 올바르지 않은 것
        return False
    
    s = list(s)[::-1]
    #매개변수를 스택(방향이 하나)으로 사용하기 위해 뒤집고, 리스트로 변환
    cnt = 0

    while s :
        tmp = s.pop()
        if tmp == '(' :            
            cnt+=1
        elif tmp == ')' :
            if cnt <= 0 :
                return False
            else : cnt -=1
    #다 돌았을 때 올바르다면 cnt = 0 
    return False if cnt else True