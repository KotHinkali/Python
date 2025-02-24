ss=int(input())
ts=int(input())
p=int(input())
p=p/12
l=0
while ss<ts:
    k=ss/100*p
    ss=ss+k
    l=l+1
    print(f"{l} - {ss:.2f}")