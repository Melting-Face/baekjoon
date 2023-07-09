import string
from sys import stdin

data = stdin.readline().strip()

arr = []

for alphabet in string.ascii_lowercase:
    arr.append(str(data.find(alphabet)))

print(" ".join(arr))