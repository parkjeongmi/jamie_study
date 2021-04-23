#프로그래머스
#그리디
#큰 수 만들기

#목표 : number에서 k개의 수를 제거했을 때 가장 큰 숫자 만들기
#알고리즘 1. 이전 숫자보다 더 큰 숫자가 나오는 경우 찾기
#알고리즘 2. 이전 숫자 제거하기
#알고리즘 3. k개 제거할 때까지 반복
#알고리즘 4. k > 0 인데 못찾았으면 뒤에서부터 k개 제거하기

number = "4177252841"
k = 4

def solution(number, k):
    new = []
    for i, num in enumerate(number) :
        while(k>0 and len(new)>0 and new[-1] < num):
            new.pop()
            k-=1
        if k == 0 :
            new += list(number[i:])
            break
        new.append(num)
    new = new[:-k] if k>0 else new
    answer = ''.join(new)
    return answer
print(solution(number,k))