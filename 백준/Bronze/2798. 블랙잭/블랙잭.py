from sys import stdin

data = [[int(text) for text in line.split()] for line in stdin.readlines()]

cards = data[1]
card_size = data[0][0]
card_value = data[0][1]

card_set = set()

for i in range(card_size - 2):
    for j in range(i + 1, card_size - 1):
        for k in range(j + 1, card_size):
            total = cards[i] + cards[j] + cards[k] 
            if total <= card_value:
                card_set.add(cards[i] + cards[j] + cards[k])

print(min(card_set, key=lambda x: abs(x - card_value)))