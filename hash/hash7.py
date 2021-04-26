#프로그래머스
#해시
#베스트 앨범

#테스트 부분 실패 (중복일 경우)

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

#알고리즘1. 장르를 key로 plays를 value로 dic 만들기
di = {}
for g, p in zip(genres, plays) :
    if g not in di.keys() :
        di[g] = [p]
    else : di[g].append(p)

#알고리즘2. (1) 장르별 재생 횟수 (2) 재생 횟수 (3) 번호
#알고리즘2-1. 장르별 재생 횟수 합 구해서 정렬하기

#재생 횟수가 같다면 번호가 작은 것부터 출력
for i in sorted(di.keys(), key = lambda x : sum(di[x]), reverse= True) :
    for j in range(len(di[i])) :
        c = 0
        if di[i][j] < di[i][j+1] :
            c = di[i][j+1]
            di[i][j+1] = di[i][j]
            di[i][j] = c
        else : 


print(answer)