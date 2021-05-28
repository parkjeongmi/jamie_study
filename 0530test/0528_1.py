#해시
#프로그래머스
#베스트앨범

genres = 	["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	

# total = {'classic' : 1450, 'pop' : 3100}
# index = { 'classic' : [(500, 0), (150, 2), (800, 3)], 'pop' : [(600, 1), (2500, 4)]}

def solution(genres, plays):
    total = {}
    index = {}
    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]
        total[genre] = total.get(genre, 0) + play
        index[genre] = index.get(genre, []) + [(play, i)]
    print(index)
    total_sort = sorted(total.items(), key = lambda x : x[1], reverse=True)
    answer = []
    for (g, p) in total_sort :
        index[g] = sorted(index[g], key = lambda x : (-x[0], x[1]))
        answer += [i for (play, i) in index[g][:2]]
    return answer


def solution(genres, plays):
    dict = {}
    #0. {장르 : 재생 횟수} 사전
    for i in range(len(genres)) :
        if genres[i] not in dict.keys() :
            dict[genres[i]] = [plays[i]]
        else :
            dict[genres[i]].extend([plays[i]])

    #1.장르 크기 순
    genres_plays = {}
    size = []
    for key, value in dict.items() :
        genres_plays[key] = sum(value)
    size = sorted(genres_plays.items(), key = lambda x : x[1], reverse=True)

    #2. 리스트 안에서 max 최대 두 개 추출
    answer = []
    for i in size :
        value = dict[i[0]]
        if len(value) > 1 :
            value.sort(reverse=True)
            answer.extend(value[:2])
        else :
            answer.extend(value)

    #3. 해당 횟수 index 출력
    final = []
    for a in answer :
        for index, value in enumerate(plays) :
            if a == value : 
                final.append(index)
    return final