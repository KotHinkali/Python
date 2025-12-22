list1=list(map(int,input().split()))
a=int(input())
b=0
while b!= len(list1):
    if list1[b] >=a:
        b+=1
    else:
        print(b+1)
        break