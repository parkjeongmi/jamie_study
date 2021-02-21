#5회의 카드 게임, 각 게임의 득점 -> 총점 구하기

#입력 ; n개의 점수 (한줄씩 입력, 5개 입력)
#출력 : 점수의 합

score = []
for _ in range(5) : score.append(int(input()))
sum = 0
for i in score :
    sum=sum+i
print(sum)