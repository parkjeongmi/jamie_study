#프로그래머스
#해시
#전화번호목록

#목표 : 한 원소가 다른 원소에 포함될 경우를 check 하기
#알고리즘1. phone_book을 해시로 만들기 (d = {})
#알고리즘2. d의 key 값과 phone_book을 비교해서 값이 포함되는지 확인 -> phone을 하나씩 넣으면서 앞이 같으면 같은 key로 만든다
#알고리즘3. 값이 포함되면 value를 바꾸기 -> dic을 확인하면서 key의 크기가 2 이상인 것의 원소 끼리 접두어인지 check함
#알고리즘4. value의 값이 뭐보다 크면 false 출력 -> 접두어이면 false


#틀린 부분 : di[phone[0]] = [phone] 에서 배열로 안넣어서 else일 경우 append를 못함
#배운점 : not in di.keys()로 key 확인하기
#배운점 : 슬라이싱으로 접두어 확인하기

phone_book = ["119", "97674223", "1195524421"]
di = {}
#알고리즘1. dictionary로 구성해서 첫 글자가 같은 것 끼리 묶기
for phone in phone_book :
    if phone[0] not in di.keys() :
        di[phone[0]] = [phone]
    else : di[phone[0]].append(phone)

#알고리즘2. 첫 글자가 같은 것 -> 리스트 길이 비교해서 접두어인지 확인하기
for key in di.keys() :
    if len(di[key]) == 1 :
        continue
    elif len(di[key]) > 1 :
        for i in range(len(di[key])) :
            for j in range(len(di[key])) :
                if (di[key][i] < di[key][j]) and (di[key][j][0:len(di[key][i])] == di[key][i]) :
                    print(False)
print(True)





# d = {}
# for key in phone_book :
#     d[key] = 0
        
#문제 : 다음 값이랑 비교 어떻게 함? -> for문으로 돌자 
# keys = list(d.keys())
# index = 0
# for i in phone_book :
#     for k in keys : 
#         if i != k :
#             if 'i' in k :
#                 d[keys[i]] = 1
# answer = [v for k, v in d.items() if v > 0]
# print(d)

# if len(answer) > 0 : return print('false')
# else : return print('true')