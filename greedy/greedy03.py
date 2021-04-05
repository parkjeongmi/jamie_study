#프로그래머스
#그리디
#큰 수 만들기
def solution(number, k) :
    number_ing = []
    for i in number :
        number_ing.append(i)
    number_ing.sort(reverse=True)
    while (len(number_ing) != k ) :
        del number_ing[len(number_ing)]
    for i in number_ing :
        return ''.join(i)

number = "19245" 
k = 2
print(solution(number,k))
#문자열 형식으로 숫자 number, 제거할 수의 개수 k -> number에서 k 개의 수 제거

def answer(number, k) : 
    number_ing = []
    for i, num in enumerate(number) :
        while len(number_ing) > 0 and number_ing[-1] < num and k > 0 :
            number_ing.pop()
            k-=1
        if k == 0 :
            number_ing += list(number[i:])
            break
        number_ing.append(num)
    number_ing = number_ing[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer