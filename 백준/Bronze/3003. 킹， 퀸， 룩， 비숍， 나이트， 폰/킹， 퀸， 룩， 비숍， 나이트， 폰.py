from sys import stdin

data = [int(text) for text in stdin.readline().strip().split()]

chess = [1, 1, 2, 2, 2, 8]

arr = []

for idx, num in enumerate(data):
    arr.append(str(chess[idx] - num))

print(" ".join(arr))