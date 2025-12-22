#a,b,n=list(map(int, input().split()))
#print(n+((n-1)//a)*b)

#a,b,c=list(map(int,input().split()))
#print((a+b+c)-min(a+b,a+c,b+c,(a+b+c)//2))

#def mam(m,p):
    ###################nt(input())
#mam(

import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it); k = next(it)
    w = [next(it) for _ in range(n)]
    p = [next(it) for _ in range(n)]

    w.sort(reverse=True)   # от тяжёлых к лёгким
    p.sort()               # от малых к большим

    heap = []  # max-heap через хранение отрицательных значений
    j = 0
    total = 0

    for wi in w:
        limit = k // wi
        while j < n and p[j] <= limit:
            heapq.heappush(heap, -p[j])
            j += 1
        if not heap:
            print(-1)
            return
        pj = -heapq.heappop(heap)
        total += wi * pj

    print(total)

if __name__ == "__main__":
    main()