from sys import stdin

nums = [int(x) for x in stdin.readlines()]
nums = nums[:-1]

max_num = max(nums)

dp = [0, 1, 1]

if max_num > 2:
    for i in range(3, max_num + 1):
        dp.append(dp[i - 2] + dp[i - 1])

for idx, num in enumerate(nums):
    print(f"Hour {num}: {dp[num]} cow(s) affected")