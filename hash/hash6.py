#프로그래머스
#해시
#위장

#알고리즘1. 의상의 종류(1번째)를 key로 의상의 이름(0번째)는 append하기
#알고리즘2. di에서 하나 이상을 택하는 경우의 수

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    di = {}
    for i in clothes : 
        if i not in di.keys() :
            di[i[1]] = [i[0]]
        else : di[i[1]].append(i[0])
    result = 1
    for key in di.keys() :
        result *= (len(di[key]) + 1)
    return result-1
