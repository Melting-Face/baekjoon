from sys import stdin

data = [[int(text) for text in line.split()] for line in stdin.readlines()]

for first, second in data:
    try:
        share, remainder = divmod(first, second)
        if remainder == 0:
            print('multiple')
            continue

        share, remainder = divmod(second, first)
        if remainder == 0:
            print('factor')
            continue

        print('neither')
    except ZeroDivisionError as ze:
        pass