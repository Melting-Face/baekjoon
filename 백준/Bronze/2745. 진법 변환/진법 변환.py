import string
from sys import stdin

nums = "0123456789" + string.ascii_uppercase

data = [text.strip() for text in stdin.readline().split()]

total = 0
num = int(data[1])

for idx, text in enumerate(data[0][::-1]):
    total += (nums.index(text) * (num ** idx))

print(total)