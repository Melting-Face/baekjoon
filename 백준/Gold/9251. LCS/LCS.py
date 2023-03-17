import sys
read = sys.stdin.readline

str1, str2 = read().strip(), read().strip()

str1_len = len(str1)
str2_len = len(str2)

arr = [[0 for j in range(str2_len + 1)] for i in range(str1_len + 1)]
for i, s1 in enumerate(str1):
    for j, s2 in enumerate(str2):
        if s1 == s2:
            arr[i + 1][j + 1] = arr[i][j] + 1
        else:
            arr[i + 1][j + 1] = max(arr[i][j + 1], arr[i + 1][j])
print(arr[str1_len][str2_len])