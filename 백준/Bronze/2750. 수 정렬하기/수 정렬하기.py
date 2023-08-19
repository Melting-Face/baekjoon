from sys import stdin

nums = [int(text) for text in stdin.readlines()]

sorted_nums = sorted(nums[1:])

for num in sorted_nums:
    print(num)