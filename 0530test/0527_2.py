#해시
#프로그래머스
#완주하지 못한 선수

participant = ["a", "a", "b"]
completion = ["a", "a"]
dict = {}
for p in participant :
    if p in dict.keys() :
        dict[p] += 1
    else :
        dict[p] = 1

for c in completion :
    if c in dict.keys() :
        dict[c] -= 1
    
for key, value in dict.items() :
    if value != 0 :
        print(key)

        