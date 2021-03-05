#프로그래머스
#그리디
#체육복

#lost = 도난당한 학생의 번호
#reverse = 여벌의 체육복
#최대 학생 수
#array 에 다 합치고, lost 와 reverse 돌리면서 보기 

n=5
lost = [2,4]
reserve = [1,3,5]


#시간초과
# def solution(n, lost, reserve):
#     student = 0
#     all = ['null']*(n+2)
#     for i in lost :
#         all[i] = 'X'
#     for i in reserve :
#         all[i] = 'O'
    
#     i = 0
#     while(i<(len(all)+1)) :
#         if all[i] == 'X' :
#             if all[i+1] == 'O' :
#                 student+=1
#                 i += 2
#         elif all[i] == 'O' :
#             if all[i+1] == 'X' :
#                 student+=1
#                 i+=2
#         else : i+=1
#     answer = student
#     return answer
# print(solution(n, lost, reserve))

def solution(n, lost, reserve) :
    #로직 : 전체 학생에서 체육복이 없는 학생 제외하기
    #여유가 있는 학생들 앞 뒤로 살펴, 체육복 빌려주기 (어레이에서 제외)

    new_reserve = [r for r in reserve if r not in lost]
    # 잃어버리지 않은, 여유가 있는 학생

    new_lost = [l for l in lost if l not in reserve]
    # 여유가 있지 않은, 체육복이 없는 학생

    for r in new_reserve :
    # r = 여유가 있는 학생들을 돌기
        front = r-1
        back = r+1
        # 여유가 있는 학생들 앞, 뒤로 살피기
        if front in new_lost : 
            new_lost.remove(front)
        elif back in new_lost :
            new_lost.remove(back)
    answer = n-len(new_lost)
    #전체 학생에서 체육복이 없는 학생을 빼서 구하기
    return answer


