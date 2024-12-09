with open("nine.txt", "r") as read:
  data = list(map(int, list(read.read())))
temp = data.copy()

def one():
  last_even = len(data) - 1
  if last_even % 2 == 1:
    last_even -= 1
  total = 0
  pos = 0
  for i, d in enumerate(data):
    if i % 2 == 0:
      total += (i / 2) * (pos * 2 + d - 1) * d / 2
      pos += d
      data[i] = 0
    else:
      while data[last_even] != 0 and data[last_even] <= d:
        total += (last_even / 2) * (pos * 2 + data[last_even] - 1) * data[last_even] / 2
        d -= data[last_even]
        pos += data[last_even]
        data[last_even] = 0
        last_even -= 2
      if data[last_even] == 0:
        break
      diff = data[last_even] - d
      total += (last_even / 2) * (pos * 2 + d - 1) * d / 2
      pos += d
      data[last_even] = diff
  print(int(total))

def two():
  last_even = len(data) - 1
  if last_even % 2 == 1:
    last_even -= 1
  total = 0
  pos = 0
  gaps = []
  for i, d in enumerate(data):
    if i % 2 == 1:
      gaps.append((pos, d))
    pos += d
  for i, d in reversed(list(enumerate(data[::2]))):
    for j in range(len(gaps)):
      if gaps[j][1] >= d and j < i:
        total += i * (gaps[j][0] * 2 + d - 1) * d / 2
        data[i * 2] = -d
        gaps[j] = (gaps[j][0] + d, gaps[j][1] - d)
        break
  pos = 0
  for i, d in enumerate(data):
    if i % 2 == 0 and d > 0:
      total += (i / 2) * (pos * 2 + d - 1) * d / 2
      data[i] = 0
    pos += abs(d)
  print(int(total))
      
one()
data = temp
two()