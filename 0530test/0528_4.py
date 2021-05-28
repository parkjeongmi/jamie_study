#프로그래머스
#정렬
#K번쨰 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer =[]
for c in commands :
    i = c[0]
    j = c[1]
    k = c[2]
    now = sorted(array[i-1:j])
    answer.append(now[k-1])
print(answer)