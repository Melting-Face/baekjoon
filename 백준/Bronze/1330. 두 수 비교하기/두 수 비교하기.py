from sys import stdin

A, B = [int(data) for data in stdin.readline().split()]

rst = '=='
if A < B:
    rst = '<'
elif A > B:
    rst = '>'

print(rst)