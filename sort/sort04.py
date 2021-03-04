#이것이 코딩 테스트다
#정렬
#2. 위에서 아래로

#큰 수 부터 작은 수의 순서 (내림차순)
n = int(input())
array = []
for i in range(n) : array.append(int(input()))

array.sort(reverse=True)
for i in array : print(i, end=' ')

#print 안에 end = ' '를 넣으면 한 칸 띄고 출력