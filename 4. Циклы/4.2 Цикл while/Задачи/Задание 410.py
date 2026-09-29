m = -float("inf")
k = 0
while (n := int(input())) != 0:
    k += 1
    if n > m:
        m=n
print(m, k)
