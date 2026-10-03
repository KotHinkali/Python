m = 0
k = 0
max_len = 0
while (n := int(input())) != 0:
    if m == n:
        k += 1
    else:
        k = 1
    if k > max_len:
        max_len = k
    m = n
print(max_len)
