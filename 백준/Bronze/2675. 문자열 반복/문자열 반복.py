from sys import stdin

data = [[text for text in line.split()] for line in stdin.readlines()]

for num, words in data[1:]:
    output = ""
    for word in words:
        output += (word * int(num))
    print(output)