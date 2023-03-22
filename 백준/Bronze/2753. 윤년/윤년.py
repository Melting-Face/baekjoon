from sys import stdin

year = int(stdin.readline())

rst = 0

if not year % 400 or (not year % 4 and year % 100):
    rst = 1

print(rst)