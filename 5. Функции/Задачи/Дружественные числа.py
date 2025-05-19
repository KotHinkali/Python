def is_friends(num1, num2):
    k = 0
    k1 = 0
    for i in range(1,num1):
        if num1 % i == 0:
            k += i
    for j in range(1,num2):
        if num2 % j == 0:
            k1 += j
    return num1 == k1 and num2 == k


a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in range(i+1, b + 1):
        if is_friends(i,j):
            print(f"({i}, {j})",end=' ')