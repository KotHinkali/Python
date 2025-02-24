a = int(input())
b = int(input())
c = int(input())
h = max(a, b, c)
k1 = min(a, b, c)
k2 = (a + b + c) - h - k1
if k1 + k2 <= h:
    print("Не существует")
elif k2 ** 2 + k1 ** 2 > h ** 2:
    print("Острый")
elif k2 ** 2 + k1 ** 2 < h ** 2:
    print("Тупой")
elif k2 ** 2 + k1 ** 2 == h ** 2:
    print("Прямоугольный")
