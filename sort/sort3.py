def solution(citations):
    answer = len(citations) 
    citations.sort()
    
    while(1) :
        count = 0
        for i in citations :
            if i >= answer :
                count+=1
            if answer <= count :
                return answer
        answer-=1
    return answer