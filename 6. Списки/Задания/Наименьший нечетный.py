lst=list(map(int, input().split()))
a=10000000
for i in range(len(lst)):
    if lst[i]<a and lst[i]%2!=0:
        a=lst[i]
if a==10000000:
    print(0)
else:
    print(a)