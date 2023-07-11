from sys import stdin

data = [[int(text) for text in line.split()] for line in stdin.readlines()]

arr1 = data[1: 1 + data[0][0]]
arr2 = data[1 + data[0][0]:]

for i in range(data[0][0]):
    arr = []
    for j in range(data[0][1]):
        arr.append(str(arr1[i][j] + arr2[i][j]))

    print(" ".join(arr))