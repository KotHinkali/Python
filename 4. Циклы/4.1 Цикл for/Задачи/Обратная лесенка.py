n = int(input())
for i in range(n, 0, -1):
    for j in range(0, i):
        print(n - j, end="")
    print()
