from sys import stdin

rows = [line.strip() for line in stdin.readlines()]

max_text_length = len(max(rows, key=lambda row: len(row)))

return_text = ""

for index in range(max_text_length):
    for row in rows:
        try:
            return_text += row[index]
        except IndexError as ie:
            pass

print(return_text)