from sys import stdin

nums = [int(x) for x in stdin.readlines()]

max_num = max(nums)

dp = [1, 1]

if max_num > 1:
    for i in range(2, max_num + 1):
        dp.append(dp[i - 2] + dp[i - 1])

for num in nums[1:]:
    print(dp[num])