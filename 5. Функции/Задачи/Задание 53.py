def is_palindrome(num):
    return str(num)==str(num)[::-1]
a=int(input())
b=int(input())
k=0
for i in range(a,b+1):
    if is_palindrome(i):
        print(i, end=" ")
        k+=1
if k==0:
    print("Нет палиндромов")
