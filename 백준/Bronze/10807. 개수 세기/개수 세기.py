from sys import stdin

data = [[int(data) for data in line.split()] for line in stdin.readlines()]

count = 0

for num in data[1]:
    if num == data[2][0]:
        count += 1

print(count)