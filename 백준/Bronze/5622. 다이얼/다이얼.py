import string
from sys import stdin

data = stdin.readline().strip()

case_dict = {}

idx = 3

for uppercase in string.ascii_uppercase:
    case_dict[uppercase] = idx

    if uppercase == "C":
        idx += 1
    elif uppercase == "F":
        idx += 1
    elif uppercase == "I":
        idx += 1
    elif uppercase == "L":
        idx += 1
    elif uppercase == "O":
        idx += 1
    elif uppercase == "S":
        idx += 1
    elif uppercase == "V":
        idx += 1

total = 0

for word in data:
    total += case_dict.get(word)

print(total)