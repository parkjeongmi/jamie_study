#제곱근

n = 1
list = [i**2 for i in range(1, n+1)]
if n > 1 :
    for i in range(2,n+1) :
        for j in range(2,n+1) :
            now = pow(i,j)
            if now <= pow(n,2) and now not in list :
                list.append(now)
list.sort()
print(list[n-1])