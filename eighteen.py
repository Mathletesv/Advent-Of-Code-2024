from collections import deque

with open("eighteen.txt", "r") as read:
    coords = []
    for line in read:
        coords.append(list(map(int, line.split(','))))

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def test(bytes):
    size = 71
    grid = [['.' for i in range(size)] for i in range(size)]
    visited = [[-1 for i in range(size)] for i in range(size)]
    for i in range(bytes):
        grid[coords[i][1]][coords[i][0]] = '#'
    visited[0][0] = 0
    bfs = deque()
    bfs.append((0, 0))
    while len(bfs) > 0:
        next = bfs.popleft()
        if next[0] == next[1] == size - 1:
            return visited[next[1]][next[0]]
        for d in dirs:
            if 0 <= (d[1] + next[1]) < size and 0 <= (d[0] + next[0]) < size:
                if grid[d[1] + next[1]][d[0] + next[0]] == '.' and visited[d[1] + next[1]][d[0] + next[0]] < 0:
                    visited[d[1] + next[1]][d[0] + next[0]] = visited[next[1]][next[0]] + 1
                    bfs.append((d[0] + next[0], d[1] + next[1]))
    return -1

def one():
    print(test(1024))  

def two():
    lo, hi = 0, len(coords)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if test(mid) == -1:
            hi = mid
        else:
            lo = mid
    if test(lo) == -1:
        print(coords[hi])
    else:
        print(coords[lo])

one()
two()