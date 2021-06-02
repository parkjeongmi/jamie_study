#프로그래머스
#멀쩡한 사각형

#w * h - ( h  * 2 - gcd * 2)
#w * h - w - h + gcd
#w * h - gcd

w = 8
h = 12

from math import gcd

g = gcd(w, h)
print(w*h-w-h+g)

