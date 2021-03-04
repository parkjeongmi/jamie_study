#이것이 코딩 테스트다
#정렬
#4. 두 배열의 원소 교체

n, k = map(int, input().split())
list_n = list(map(int, input().split()))
list_k = list(map(int, input().split()))

list_n.sort()
list_k.sort(reverse=True)
for i in range(k) :
    list_n[i], list_k[i] = list_k[i], list_n[i]
print(sum(list_n))