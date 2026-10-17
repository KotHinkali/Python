def phib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return phib(n-1)+phib(n-2)
n=int(input())
print(phib(n))