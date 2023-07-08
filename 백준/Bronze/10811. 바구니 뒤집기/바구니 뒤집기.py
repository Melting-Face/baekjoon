from sys import stdin

data = [[int(text) for text  in line.split()] for line in stdin.readlines()]

arr = [str(idx) for idx in range(1, data[0][0] + 1)]

for start, end in data[1:]:
    arr[start-1: end] = reversed(arr[start-1: end])

print(" ".join(arr))