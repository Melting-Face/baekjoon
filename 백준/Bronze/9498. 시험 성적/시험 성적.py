from sys import stdin

score = int(stdin.readline())

rst = 'F'
if 90 <= score <= 100:
    rst = 'A'
elif 80 <= score <= 89:
    rst = 'B'
elif 70 <= score <= 79:
    rst = 'C'
elif 60 <= score <= 69:
    rst = 'D'

print(rst)