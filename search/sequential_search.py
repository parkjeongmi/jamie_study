#순차탐색 : 앞에서부터 하나씩 차례대로

def sequential_search(n, target, array) :
    for i in range(n) :
        if array[i] == target :
            return i+1
    
print("생성할 원소의 개수")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("문자열 입력")
array = input().split()

print(sequential_search(n, target, array))