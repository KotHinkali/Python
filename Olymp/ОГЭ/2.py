n=int(input())
a=[int(input()) for i in range(n)]
b=[x for x in a if x%7==1]
print(sum(b))