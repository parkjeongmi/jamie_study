#프로그래머스
#DFS, BFS
#타겟넘버

#목표 : 타겟 넘버를 만드는 방법의 수 return

numbers = [1,2,3]
target = 4
answer_list = [0]
for i in numbers : 
    temp = []
    for j in answer_list :
        temp.append(j+i)
        temp.append(j-i)
    answer_list = temp
answer = answer_list.count(target)
print(answer)