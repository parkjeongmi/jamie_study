#프로그래머스
#그리디
#조이스틱

#return : 조이스틱 조작 값의 최소 값

name = str(input())

def solution(name) :
    #change에서 부터 min 값을 골라 넣음
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) +1) for i in name]
    idx = 0
    answer = 0

    while True :
        answer += change[idx]
        change[idx] = 0
        #change 안의 값이 다 0이 되면, 정답 반환
        if sum(change) == 0 :
            return answer

        left, right = 1, 1
        #이동한 값이 0이라면, 두 칸/세 칸 +1칸만큼 더 이동
        while change[idx - left] == 0 :
            left +=1 
        while change[idx + right] == 0 :
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right
        




# def solution(name) :
#     n = len(name)
#     answer = []
#     answers = 0
#     for i in name :
#         number_i = ord(i)
#         if number_i >= 79 :
#             answer.append(abs(number_i-92))
#             answers+=abs(number_i-92)
#         else : 
#             answer.append(number_i - 65)
#             answers+=number_i-65
#     return answer

# print(solution(name))
