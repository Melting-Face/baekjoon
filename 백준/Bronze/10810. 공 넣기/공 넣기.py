from sys import stdin

data = [[int(data) for data in line.split()] for line in stdin.readlines()]

arr = ['0'] * data[0][0]
for d in data[1:]:
    start = d[0] - 1
    end = d[1]
    for idx in range(start, end):
        arr[idx] = str(d[2])

print(" ".join(arr))