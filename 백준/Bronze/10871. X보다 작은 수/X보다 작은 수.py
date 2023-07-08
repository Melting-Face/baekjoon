from sys import stdin

data = [[int(num) for num in line.split()] for line in stdin.readlines()]

arr = []
for d in data[1]:
    if d < data[0][1]:
        arr.append(str(d))
        
print(' '.join(arr))