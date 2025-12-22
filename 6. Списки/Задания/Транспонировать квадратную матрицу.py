def transpose(a):
    c=[]
    for i in range(len(a)):
        k = []
        for j in range(len(a[i])):
            k.append(a[j][i])
        c.append(k)
    return c


n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
print(transpose(m))