nums=list(map(int,input().split()))
def shift_right(lst):
    return lst[-1::]+lst[:-1]


def shift_left(lst):
    return lst[1::]+lst[:1]

print(shift_left(nums))
print(shift_right(nums))


