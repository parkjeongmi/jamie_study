#숫자를 한글로 변환하기
#logic
#1. 일의 자리는 단위를 붙여읽지 않는다 ex. 일 이 삼 사
#2. 일/십/천/백 등 0으로 끝나면, 자리를 안 읽음
#3. 십/백/천의 자리는 숫자를 읽은 글자와 단위 글자를 붙여준다

def readNumber(n) :
    units = [' '] + list('십백천')
    nums = '일이삼사오육칠팔구'
    result = []
    i = 0
    while n>0 :
        n, r = divmod(n, 10)
        if r > 0 :
            result.append(nums[r-1] + units[i])
        i+=1

    return ''.join(result[::-1])
