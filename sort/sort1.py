#프로그래머스
#sort
#K번째수

def solution(array, commands):
    answer = []
    for index in commands :
        list = []
        end = index[1]
        start = index[0]
        k = index[2]
        while (start<=end) : 
            list.append(array[start-1])
            start+=1
        list.sort()
        answer.append(list[k-1])
    return answer


def solution(array, commands) :
    answer = []
    for command in commands : 
        i, j, k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer