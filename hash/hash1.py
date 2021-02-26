#프로그래머스
#해시
#완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    num = len(completion)
    for i in range(num) :
            if participant[i] != completion[i] :
                return participant[i]
    return participant[num]


def solution2 (participant, completion) :  
    answer = ''
    temp = 0
    dic = {}
    for i in participant :
        dic[hash(i)] = i
        temp += int(hash(i))
    for j in completion :
        temp -= hash(j)
    answer = dic[temp]

    return answer