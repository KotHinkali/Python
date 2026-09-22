a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print("гриб")
elif 2 <= a % 10 <= 4 and not(12<=a%100<=15):
    print("гриба")
else:
    print("грибов")