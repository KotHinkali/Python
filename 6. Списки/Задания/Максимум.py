n,m=list(map(int, input().split()))
matrix= [list(map(int, input().split())) for i in range(n)]
a_max=0
j_max=0
for i in range(n):
    for j in range(m):
        if matrix[i][j]>matrix[a_max][j_max]:
            a_max=i
            j_max=j
print(a_max,j_max)


