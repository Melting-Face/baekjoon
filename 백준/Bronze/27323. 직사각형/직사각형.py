from sys import stdin

data = [int(line.strip()) for line in stdin.readlines()]

print(data[0] * data[1])