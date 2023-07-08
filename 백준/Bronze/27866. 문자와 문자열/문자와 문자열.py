from sys import stdin

data = [line for line in stdin.readlines()]

print(data[0][int(data[1]) - 1])