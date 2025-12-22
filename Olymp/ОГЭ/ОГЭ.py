a=int(input())
b=0
while a!=0:
    if a%2==0 and a%5==0:
        b+=1
    a = int(input())
print(b)
