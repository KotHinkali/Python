a=int(input())
ml=1
nl=1
d=0
while a!=0:
    z=int(input())
    if z==0:
        break
    if z>a:
        if d==1:
            nl+=1
        else:
            nl=2
        d=1
    elif z<a:
        if d==-1:
            nl+=1
        else:
            nl=2
        d=-1
    else:
        nl=1
        d=0
ml=max(ml,nl)
print(ml)