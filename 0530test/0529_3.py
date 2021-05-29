#프로그래머스
#문자열 압축

#이게 2단계라고..?

s = "aabbaccc"

max = 0
result = ""
length = []
for cut in range(1,(len(s)//2+1)) :
    #cut는 압축 횟수
    temp = s[:cut]
    count = 1
    for i in range(cut, len(s), cut) :
        if s[i:i+cut] == temp :
            count+=1
        else :
            if count == 1 :
                count = ""
            result += str(count) + temp
            temp = s[i:i+cut]
            count = 1
    if count == 1 :
        count = ""
    result += str(count) + temp
    length.append(len(result))
    result = ""
print(min(length))