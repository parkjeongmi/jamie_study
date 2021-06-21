#구현
#별찍기4

n = int(input())

for i in range(0, n) :
    print(" " * i + "*"*(n-i))