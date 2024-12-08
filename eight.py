from math import gcd

with open("eight.txt", "r") as read:
  data = read.read().split("\n")
  anti = [[False for i in range(len(data[0]))] for i in range(len(data))]

def try_add(i, j):
  if 0 <= i < len(data) and 0 <= j < len(data[0]):
    anti[i][j] = True

def one():
  nodes = {}
  for i in range(len(data)):
    for j in range(len(data[i])):
      c = data[i][j]
      if c == ".":
        continue
      if c not in nodes:
        nodes[c] = set()
      for (row, col) in nodes[c]:
        try_add(2 * row - i, 2 * col - j)
        try_add(2 * i - row, 2 * j - col)
      nodes[c].add((i, j))
  print(sum(1 for line in anti for c in line if c))

def add_all(i, j, r, c):
  x = i - r
  y = j - c
  g = gcd(x, y)
  x //= g
  y //= g
  r, c = i, j
  while 0 <= r < len(data) and 0 <= c < len(data[0]):
    anti[r][c] = True
    r += x
    c += y
  r, c = i, j
  while 0 <= r < len(data) and 0 <= c < len(data[0]):
    anti[r][c] = True
    r -= x
    c -= y
    

def two():
  nodes = {}
  for i in range(len(data)):
    for j in range(len(data[i])):
      c = data[i][j]
      if c == ".":
        continue
      if c not in nodes:
        nodes[c] = set()
      for (row, col) in nodes[c]:
        add_all(i, j, row, col)
      nodes[c].add((i, j))
  print(sum(1 for line in anti for c in line if c))

one()
anti = [[False for i in range(len(data[0]))] for i in range(len(data))]
two()