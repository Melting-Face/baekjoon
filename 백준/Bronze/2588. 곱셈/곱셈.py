from sys import stdin

A, B = [int(data) for data in stdin.readlines()]

total = A * B

remains = []

while B >= 10:
    B, remain = divmod(B, 10)
    remains.append(remain)

remains.append(B)

for remain in remains:
    print(remain * A)

print(total)