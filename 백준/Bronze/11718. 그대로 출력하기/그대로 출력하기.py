from sys import stdin

data = [line.strip() for line in stdin.readlines()]

for word in data:
    print(word)