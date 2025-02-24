def print_seq(begin, end):
    for i in range(begin, end + 1):
        print(i, end=' ')
    print()


def sum_seq(begin, end):
    s = 0
    for i in range(begin, end + 1):
        s += i
    return s



a = 4
b = 25

print(sum_seq(1, 10))