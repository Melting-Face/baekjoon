from sys import stdin

rows = [[int(text) for text in line.split()] for line in stdin.readlines()]

max_row = None
max_col = None
max_value = -1

for i, row in enumerate(rows):
    for j, num in enumerate(row):
        if num > max_value:
            max_value = num
            max_row = i
            max_col = j

print(max_value)
print(f"{max_row + 1} {max_col + 1}")