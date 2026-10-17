def b(x):
    print(bin(x)[2:])


def bi(x):
    if x>1:
        bi(x//2)
    print(x%2, end="")

x=int(input())
bi(x)

