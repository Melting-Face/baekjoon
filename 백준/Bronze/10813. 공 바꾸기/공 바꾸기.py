from sys import stdin

data = [[int(data) for data in line.split()] for line in stdin.readlines()]

arr = [str(idx + 1) for idx in range(data[0][0])]

for start, end in data[1:]:
    arr[end - 1], arr[start - 1] = arr[start - 1], arr[end - 1]

print(" ".join(arr))