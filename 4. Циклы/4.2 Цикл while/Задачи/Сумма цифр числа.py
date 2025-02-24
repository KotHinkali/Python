n=int(input())
s=0
while n!=0:
    k=n%10
    s=s+k
    n=n//10
print(s)