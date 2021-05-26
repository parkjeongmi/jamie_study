#스택_기본

# stack = []
# stack.append('a')
# stack.append('b')
# stack.append('c')

# stack.pop()
# print(stack)

#큐_기본
# queue = []
# queue.append('a')
# queue.append('b')
# queue.append('c')
# print(queue.pop(0))

#스택_deque
# from collections import deque
# stack = deque()
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.pop()
# print(stack)

#큐_deque
# from collections import deque
# queue = deque()
# queue.append('a')
# queue.append('b')
# queue.append('c')

# queue.popleft()
# print(queue)

#기타 함수
from collections import deque
list = deque()
list.append('a')
list.append('b')
list.append('c')

#동일한 원소 count
# print(list.count('a'))

list.reverse()
#['c', 'b', 'a']
list.pop()
print(list)