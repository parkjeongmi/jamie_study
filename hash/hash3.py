#프로그래머스
#해시
#완주하지 못한 선수

#목표 : 첫번재 배열에 있는 모든 사람 중 두번째 배열에 없는 것 출력
#고려 : 중복 이름 -> 이름 기준으로 몇 번 보였는지 count 해야함

participant = ["leo", "leo", "eden"]	
completion = ["eden", "kiki"]

def solution(participant, completion):
    d = {}
    for key in participant :
        d[key] = d.get(key, 0) + 1
    for check in completion :
        d[check] -= 1
    
    answer = [k for k, v in d.items() if v > 0]
    return answer[0]

print(solution(participant, completion))

# scores = {"철수": 90, "민수": 85, "영희": 80}
# scores.update({"카악" : 100})
# print(scores.items())