#이것이 코딩 테스트다
#stack : 박스와 같이 차례로 쌓이는 '선입후출' 구조

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() 
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
#5 2 3 1
print(stack[::-1])
#1 3 2 5