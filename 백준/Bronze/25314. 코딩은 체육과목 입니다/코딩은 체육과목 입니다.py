from sys import stdin

input_byte = int(stdin.readline())
count = int(input_byte / 4)

output = ""

for _ in range(count):
    output += "long "

output += "int"

print(output)