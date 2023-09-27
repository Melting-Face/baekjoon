from sys import stdin

data = [int(line) for line in stdin.readlines()]

data.sort()
print(int(sum(data) / len(data)))
print(data[2])