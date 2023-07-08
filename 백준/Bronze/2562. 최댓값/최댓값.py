from sys import stdin

data = [int(line) for line in stdin.readlines()]

max_number = -1
max_index = -1

for idx, num in enumerate(data):
    if num >= max_number:
        max_number = num
        max_index = idx

print(max_number)
print(max_index + 1)