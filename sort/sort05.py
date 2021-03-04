#이것이 코딩 테스트다
#정렬
#3. 성적이 낮은 순서로 학생 출력하기

n = int(input())

array=[]
for i in range(n) :
    data = input().split()
    array.append([str(data[0]), int(data[1])])
array.sort(key=lambda x : x[1])

for i in array : print(i[0], end=' ')