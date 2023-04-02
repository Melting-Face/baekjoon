from sys import stdin

A, B = [int(data) for data in stdin.readlines()]

if A > 0 and B > 0:
    print(1)
elif A < 0 and B > 0:
    print(2)
elif A < 0 and B < 0:
    print(3)
elif A > 0 and B < 0:
    print(4)