from itertools import product

n = int(input())
k = int(input())
count = 0

for item in product('aoc', repeat=n):
    line =''.join(item)
    if line.count('a') <= k and line.count('o') <= k and line.count('c') <= k:
        count += 1
print(count)