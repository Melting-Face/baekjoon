from sys import stdin


values = [0] * 10001
first_value = True
for line in stdin:
    num = int(line.strip())
    if first_value:
        first_value = False
        continue
    values[num] += 1

for index, value in enumerate(values):
    if not value:
        continue
    for _ in range(value):
        print(index)