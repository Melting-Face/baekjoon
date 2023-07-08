from sys import stdin

data = [line.strip() for line in stdin.readlines()]

for d in data[1:]:
    print(f"{d[0]}{d[-1]}")