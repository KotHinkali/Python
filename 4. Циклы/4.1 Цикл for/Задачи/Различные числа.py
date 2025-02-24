n=int(input())
k=0
m=0
o=0
for i in range(1,n+1):
    z=int(input())
    if z==0:
        k=k+1
    elif z<0:
        m=m+1
    elif z>0:
        o=o+1
print("К-во положительных чисел: ",o)
print("К-во отрицательных чисел: ", m)
print("К-во чисел, равных нулю: ", k)