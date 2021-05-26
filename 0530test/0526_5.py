#스택/큐
#프로그래머스
#기능개발

progresses = [93, 30, 55]
speeds = [1, 30, 5]

from collections import deque
import math

jobs = deque()
for i in range(len(progresses)) :
    jobs.append(math.ceil((100 - progresses[i] ) / speeds[i]))

count = []
functions = []
while len(jobs) != 0 :
    count.append(jobs.popleft())
    if len(jobs) > 0 : 
        while jobs[0] <= count[0] :
            count.append(jobs.popleft())
            if len(jobs) == 0 :
                break
    functions.append(len(count))
    count = []

print(functions)