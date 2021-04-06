#미해결
#이것이 코딩 테스트다
#정렬 : 데이터를 특정 기준에 따라 순서대로 나열하는 것
#성적이 낮은 순서로 학생 출력하기 (오름차순) 
#성적 -> 점수가 한정되어 있음 = 계수정렬이 효율적

def count_sort(data) :
    score = []
    for i in range(len(data)) :
        score.append(int(data.get(i)))
    count = [0] * 100
    for i in range(len(score)) : 
        count[score[i]] = 1
    for i in range(len(count)) : 
        if count[i] == 1 : 
            print(data.keys(i), end = ' ')

data = dict()
n = int(input())
for i in range(n) :
    input_data = input().split()
    data[input_data[0]]  = input_data[1]
#{'홍길동' : 85, '박아무개' : 92, '길다란' : 32}

count_sort(data)
