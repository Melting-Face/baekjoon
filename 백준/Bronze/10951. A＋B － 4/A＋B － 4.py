from sys import stdin

nums = [[int(data) for data in line.split()] for line in stdin.readlines()]

for num in nums:
    print(sum(num))