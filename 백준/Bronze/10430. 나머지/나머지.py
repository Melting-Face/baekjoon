import sys

A, B, C = [int(data) for data in sys.stdin.readline().split()]
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)