#프로그래머스

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

dic = {}
for p in participant :
    if p not in dic.keys() :
        dic[p] = 1
    else :
        dic[p] = 2

for com in completion :
    if com in dic.keys() :
        dic[com] -= 1
answer = 0
for key, value in dic.items() :
    if value != 0 :
        answer = key
print("".join(answer))

def solution(participant, completion):

    dic = {}
    for p in participant :
        if p not in dic.keys() :
            dic[p] = 1
        else :
            dic[p] = 2

    for com in completion :
        if com in dic.keys() :
            dic[com] -= 1
    answer = 0
    for key, value in dic.items() :
        if value != 0 :
            return(key)