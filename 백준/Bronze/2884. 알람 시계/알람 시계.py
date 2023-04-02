from sys import stdin

hour, minute = [int(data) for data in stdin.readline().split()]

if minute < 45:
    hour = hour - 1
    hour = hour if hour >= 0 else 23
    minute = 60 + minute - 45
else:
    minute = minute - 45

print(hour, minute)