from sys import stdin

data = [[int(text) for text in line.split()] for line in stdin.readlines()]

data[1].sort(reverse=True)
print(data[1][data[0][1] -1])