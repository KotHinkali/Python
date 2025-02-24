n = int(input())
m = n
k=0
while n != 0:
    k += 1
    if n>m:
        m=n
    n = int(input())
print(m, k)
