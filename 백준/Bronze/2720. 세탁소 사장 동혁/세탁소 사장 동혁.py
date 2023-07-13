from sys import stdin

data = [int(line.strip()) for line in stdin.readlines()]

coins = [25, 10, 5, 1]

for price in data[1:]:
    arr = []
    for coin in coins:
        count, price = divmod(price, coin)
        arr.append(str(count))

    print(" ".join(arr))