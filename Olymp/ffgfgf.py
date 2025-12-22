from math import*
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def meeting_time(m, p):

    meeting_time = lcm(m, p)


    if meeting_time > 10**9:
        return -1

    return meeting_time
m = int(input())
p = int(input())
print(meeting_time(m, p))
