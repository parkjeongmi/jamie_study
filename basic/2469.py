import sys

k = int(input())
n = int(input())

up = [chr(i+ord('A')) for i in range(k)]
down = list(input())

ladder = [list(input()) for i in range(n)]

for i in range(n) :
        #'?'줄의 인덱스 찾기
        if ladder[i][0] == '?' :
                break

        #시작 - ? 전까지 알파벳 변경
        for j in range(k-1) :
                if ladder[i][j] == '-' : 
                        up[j], up[j+1] = up[j+1], up[j]

for i in range(n-1, -1, -1) :
        #'?'줄의 인덱스 찾기
        if ladder[i][0] == '?' :
                break
        #끝 - ? 전까지 알파벳 변경
        for j in range(k-1) :
                if ladder[i][j] == '-' :
                        down[j], down[j+1] = down[j+1], down[j]


result = ''
for i in range(k-1) :
        #up과 down이 같으면 그대로 (*)
        if up[i] == down[i] :
                result += '*'
        #up과 down이 다르다면 바꾸고 (-)
        else :
                result += '-'
                up[i], up[i+1] = up[i+1], up[i]

if up == down :
        print(result)
#up과 down이 다른, 알 수 없는 경우는 x 출력
else : print('x' * (k-1))


