from sys import stdin

data = [[int(data) for data in line.split()] for line in stdin.readlines()]

print(f"{min(data[1])} {max(data[1])}")