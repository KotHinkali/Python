def is_perfect(num):
    m=0
    for i in range(1, num):
        if num % i == 0:
            m = m + i
    return num==m

n = int(input())
k = 0
l = 5
while k != n:
    l = l + 1
    if is_perfect(l):
        k+=1
        print(l)
