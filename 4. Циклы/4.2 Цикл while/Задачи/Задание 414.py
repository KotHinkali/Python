n = 1
m = 0
k = 0
max_len = 0
while n != 0:
    n = int(input())
    if m == n:
        k = k + 1
    else:
        k = 1
    if k>max_len:
        max_len=k
    m = n
print(max_len)
