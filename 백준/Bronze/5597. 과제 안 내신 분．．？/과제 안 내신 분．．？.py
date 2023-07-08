from sys import stdin

data = [int(line) for line in stdin.readlines()]

no_work_peoples = set(data) ^ set(range(1, 31))

for person in no_work_peoples:
    print(person)