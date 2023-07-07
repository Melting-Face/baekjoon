from sys import stdin

data = [[int(data) for data in line.split()] for line in stdin.readlines()]

max_value = max(data[1])
print(sum(data[1]) / max_value * 100 / data[0][0])