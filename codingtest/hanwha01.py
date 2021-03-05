#코드잇
#팔린드롬
#문제 : 문자열 word가 팔린드롬인지 확인하는 함수 -> true false 리턴

#1. 문자열의 첫 번째 원소와 마지막 원소, 두 번째 원소와 뒤에서 두 번째 원소의 쌍을 만들어, 이 쌍들이 서로 일치하는지 확인

#2. 문자열의 i번째 원소와 뒤에서 i 번째 원소의 쌍이 일치하는지 확인하려면 -> 둘의 합을 기준으로 수식

def is_palindrome(word) :
    for left in range(len(word) // 2) :
        right = len(word) - left -1
        if word[left] != word[right] : 
            return False
    
    return True