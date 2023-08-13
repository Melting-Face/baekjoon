from sys import stdin

N, K = [int(text) for text in stdin.readline().split()]

count = 0
isFound = False

for I in range(1, N + 1):
    share, remain = divmod(N, I)
    if remain == 0:
        count += 1

    if count == K:
        isFound = True
        print(I)
        break

if not isFound:
    print(0)