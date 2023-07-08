import re

from sys import stdin

data = stdin.readline().strip() 

words = [
  'c=',
  'c-',
  'dz=',
  'd-',
  'lj',
  'nj',
  's=',
  'z='
]
regex = '|'.join(words)
data = re.sub(regex, "0", data)
print(len(data))