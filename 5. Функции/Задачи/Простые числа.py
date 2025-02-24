def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())
k = 0
m = 2
while k < n:
    if is_prime(m):
        print(m, end=" ")
        k = k + 1
    m += 1
