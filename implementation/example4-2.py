#이것이 코딩 테스트다
#구현
#시각

n = int(input())

def solution (n) :
    hour_count, minute_count, second_count = 0,0,0
    hours = n
    minutes, seconds = 60, 60
    for hour in range(hours+1) :
        if str(hour).find('3') :
            hour_count +=1
    for minute in range(minutes+1) :
        if str(minute).find('3') :
            minute_count+=1
    for second in range(seconds+1) :
        if str(second).find('3') :
            second_count+=1
    return print(hour_count*minute_count*second_count)
        
def solution_answer(n) :
    count = 0
    for hour in range(n+1) :
        for minute in range(60) :
            for second in range(60) :
                if '3' in str(hour)+str(minute)+str(second) :
                    count+=1

    return (print(count))
solution_answer(n)