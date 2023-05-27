from sys import stdin

arr = [[int(num) for num in data.split()] for data in stdin.readlines()]

for idx, nums in enumerate(arr):
    if idx:
        print(sum(nums))