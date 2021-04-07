#이것이 코딩 테스트다
#정렬 : 데이터를 특정 기준에 따라 순서대로 나열하는 것
#성적이 낮은 순서로 학생 출력하기 (오름차순) 

n = int(input())
array = []
for i in range(n) :
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

array = sorted(array, key=lambda student: student[1])

for student in array :
    print(student[0], end = ' ')