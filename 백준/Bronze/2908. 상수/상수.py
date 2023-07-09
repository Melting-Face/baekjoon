from sys import stdin

data = [int(text[::-1]) for text in stdin.readline().strip().split()]

print(max(data))