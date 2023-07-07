from sys import stdin

data = int(stdin.readline())

for idx in range(data):
    print(" " * (data - idx - 1) + "*" * (idx + 1))