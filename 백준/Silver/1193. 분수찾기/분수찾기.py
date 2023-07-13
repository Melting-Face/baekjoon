from sys import stdin

data = int(stdin.readline().strip())

# 1. total
# 2. count
arr = [1, 0]
while True:
    arr[1] += arr[0]

    if data <= arr[1]:
        break

    arr[0] += 1

if arr[0] % 2 == 0:
    print(f"{data - arr[1] + arr[0]}/{1 - data + arr[1]}")
else:
    print(f"{1 - data + arr[1]}/{data - arr[1] + arr[0]}")