from sys import stdin

num = int(stdin.readline().strip())

for idx in range(1, 2 * num):
    print(" " * abs(num - idx) + "*" * (2 * num - 1 - 2 * abs(num - idx)))