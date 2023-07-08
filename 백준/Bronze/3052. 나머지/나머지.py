from sys import stdin

data = [int(line) % 42 for line in stdin.readlines()]

print(len(set(data)))