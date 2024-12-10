with open("ten.txt", "r") as read:
    data = [[int(x) for x in line.strip()] for line in read]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
heights = [[] for _ in range(10)]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        heights[val].append((i, j))

def one():
    tops = [[set() for _ in range(len(data[0]))] for _ in range(len(data))]

    for (i, j) in heights[9]:
        tops[i][j].add((i, j))

    def try_add(i, j, h, v):
        if 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == h - 1:
            tops[i][j].update(v)

    for h in range(9, 0, -1):
        for (i, j) in heights[h]:
            for (di, dj) in dirs:
                try_add(i + di, j + dj, h, tops[i][j])

    total = sum(len(tops[i][j]) for i, j in heights[0])
    print(total)

def two():
    tops = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    for (i, j) in heights[9]:
        tops[i][j] = 1

    def try_add(i, j, h, v):
        if 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == h - 1:
            tops[i][j] += v

    for h in range(9, 0, -1):
        for (i, j) in heights[h]:
            for (di, dj) in dirs:
                try_add(i + di, j + dj, h, tops[i][j])

    total = sum(tops[i][j] for i, j in heights[0])
    print(total)

one()
two()