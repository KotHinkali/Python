n = int(input())
m = n
k = 0
while n != 0:
    if n > m:
        m = n
        k=0
    if m == n:
        k = k + 1
    n = int(input())
print(k)
