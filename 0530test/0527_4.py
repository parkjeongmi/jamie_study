#해시
#프로그래머스
#위장
#수학 공식 문제임

clothes = [["1", "a"], ["2", "b"], ["3", "c"], ["4", "d"]]

def solution(clothes):
    dict = {}
    for clo in clothes :
        if clo[1] not in dict.keys() :
            dict[clo[1]] = [clo[0]]
        else :
            dict[clo[1]].extend([clo[0]])
    answer = 1
    for value in dict.values() :
        answer*=(len(value)+1) 
    return answer-1

def solution(clothes):
    dict = {}
    for clo in clothes :
        if clo[1] not in dict.keys() :
            dict[clo[1]] = [clo[0]]
        else :
            dict[clo[1]].extend([clo[0]])

    sum = 0
    mul = 1
    for key, value in dict.items() :
        sum += len(value)
        if len(dict.keys()) > 1:
            mul *= len(value)
        else : mul = 0
    return sum+mul

