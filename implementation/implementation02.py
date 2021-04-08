#이것이 코딩 테스트다
#구현
#시각
#각각 for문을 돌릴 경우 -> 중복 경우를 제외하기 어려움 => 3중 for문으로 한 번에 계산 필요
#3중 for문 돌렸지만, 시간, 분, 초를 각각 확인하다보니 중복 생성 => if '3' in str(i) 이용
#틀린 부분 : 문제 해석 (n이 포함된 경우라 생각했는데, 3이 포함된 경우를 계산하는 것)
#알게된 점 : 숫자를 문자열료 변형해서 in을 써서 포함 여부를 확인 가능함


n = int(input())
#00h 00m 00s -> nh 59m 59s
def count_n(n) :
    count = 0
    for i in range(n+1) :
        for j in range(0, 60) :
            for k in range(0, 60) :
                if '3' in str(i)+str(j)+str(k) :
                    count += 1
    return count

print(count_n(n))