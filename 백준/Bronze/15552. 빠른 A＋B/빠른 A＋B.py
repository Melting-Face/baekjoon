from sys import stdin

items = [[int(data) for data in line.split()] for line in stdin.readlines()]

item_length = len(items)

for idx in range(1, item_length):
    print(sum(items[idx]))