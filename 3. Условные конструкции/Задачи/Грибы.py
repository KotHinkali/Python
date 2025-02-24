a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print(a, "гриб")
elif 2 <= a % 10 <= 4 and not (a % 100 <= 12 and a % 100 <= 14):
    print(a, "гриба")
else:
    print(a, "грибов")
