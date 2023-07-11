from sys import stdin

text = stdin.readline().strip()

print(int(text == text[::-1]))