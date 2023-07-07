from sys import stdin

nums = [[int(data) for data in line.split()] for line in stdin.readlines()]

for num in nums:
    if num[0] == 0 and num[1] == 0:
        break
    print(sum(num))