# 사다리타기
import sys

#가로 막대가 없는 경우 : *
#가로 막대가 있는 경우 : -
#감추어진 특정 가로 줄 : 길이 k-1인 ?
k = sys.stdin.readline() #k = 참가한 사람의 수 
n = sys.stdin.readline() #n = 가로 줄의 수 
result = list(map(str, input().split())) #result = 참가자들의 최중 순서. 길이 k인 대문자 문자열
for i in range(n) :
        road = [*map(str, input().split())]
        print("\n")
#감추어진 가로 줄 구성