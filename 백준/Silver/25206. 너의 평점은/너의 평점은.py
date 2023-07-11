from sys import stdin

data = [[text for text in line.split()] for line in stdin.readlines()]


score_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total = 0
scores = 0

for values in data:
    if values[2] == "P":
        continue

    total += float(values[1])
    scores += score_map.get(values[2]) * float(values[1])
print(round(scores / total, 6))