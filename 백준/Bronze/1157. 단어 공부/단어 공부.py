from collections import Counter
from sys import stdin

text = stdin.readline().strip().upper()

counter = Counter(list(text))

max_value = max(counter.values())

item_list = list(filter(lambda item: item[1] == max_value, counter.items()))

if len(item_list) == 1:
    print(item_list[0][0])
else:
    print("?")