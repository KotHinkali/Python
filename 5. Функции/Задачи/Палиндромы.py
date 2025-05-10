def is_palindrome(num):
    k = 0
    m=k
    while num!=0:
        k=(k*10)+(num%10)
        num=num//10
    

a=int(input())