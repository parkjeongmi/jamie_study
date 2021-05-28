#해시
#프로그래머스
#베스트앨범

genres = 	["classic", "classic", "classic"]
plays = [500, 500, 100]

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