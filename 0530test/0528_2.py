#프로그래머스
#정렬
#H-index

citations = [0, 2, 3]
citations.sort(reverse=True)
def solution(citations):
    citations.sort(reverse=True)
    for h in range(citations[0], -1, -1) :
        sum = 0
        for c in citations :
            if c >= h :
                sum += 1
        if sum >= h :
            answer = h
            break
    return answer