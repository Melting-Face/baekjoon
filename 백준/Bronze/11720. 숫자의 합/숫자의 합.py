from sys import stdin

data = [line for line in stdin.readlines()]

nums = [int(d) for d in list(data[1].strip())]
print(sum(nums))