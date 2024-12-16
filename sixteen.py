from heapq import heappush, heappop
from collections import deque

with open("sixteen.txt", "r") as read:
    grid = []
    for line in read:
        grid.append(line)

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
    ]

def one():
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    sx, sy = -1, -1
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                sy, sx = i, j
                break
    
    pq = []

    heappush(pq, [0, 1, sy, sx])
    if grid[sy][sx - 1] != '#':
        heappush(pq, [2001, 3, sy, sx - 1])
    while len(pq) > 0:
        next = heappop(pq)
        if visited[next[2]][next[3]]:
            continue
        if grid[next[2]][next[3]] == 'E':
            print(next[0])
            return
        visited[next[2]][next[3]] = True
        d = next[1]
        for i in [-1, 0, 1]:
            y = next[2] + dirs[(d + i) % 4][1]
            x = next[3] + dirs[(d + i) % 4][0]
            if grid[y][x] != '#' and not visited[y][x]:
                heappush(pq, [next[0] + (1 if i == 0 else 1001), d + i % 4, y, x])

def two():
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    sx, sy, ex, ey = -1, -1, -1, -1
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                sy, sx = i, j
                break
    pq = []
    best = -1
    heappush(pq, [0, 1, sy, sx])
    if grid[sy][sx - 1] != '#':
        heappush(pq, [2001, 3, sy, sx - 1])
    while len(pq) > 0:
        next = heappop(pq)
        if visited[next[2]][next[3]]:
            continue
        if grid[next[2]][next[3]] == 'E':
            ey, ex = next[2], next[3]
            best = next[0]
            break
        visited[next[2]][next[3]] = True
        d = next[1]
        for i in [-1, 0, 1]:
            y = next[2] + dirs[(d + i) % 4][1]
            x = next[3] + dirs[(d + i) % 4][0]
            if grid[y][x] != '#' and not visited[y][x]:
                heappush(pq, [next[0] + (1 if i == 0 else 1001), d + i % 4, y, x])
    graph = [[[[], [], [], []] for i in range(len(grid[0]))] for j in range(len(grid))]
    visited = [[[False, False, False, False] for i in range(len(grid[0]))] for j in range(len(grid))]
    fast = [[[-1, -1, -1, -1] for i in range(len(grid[0]))] for j in range(len(grid))]
    pq = []
    heappush(pq, [0, 1, sy, sx])
    fast[sy][sx][1] = 0
    while len(pq) > 0:
        next = heappop(pq)
        if grid[next[2]][next[3]] == '#':
            print("BAD")
        if visited[next[2]][next[3]][next[1]] or fast[next[2]][next[3]][next[1]] > best:
            continue
        visited[next[2]][next[3]][next[1]] = True
        if next[2] == ey and next[3] == ex:
            continue
        d = next[1]
        y, x = next[2], next[3]
        for i in [-1, 1]:
            nd = (d + i) % 4
            if next[0] + 1000 <= best and not visited[y][x][nd] and grid[y][x] != '#':
                if (fast[y][x][nd] == -1 or fast[y][x][nd] > next[0] + 1000):
                    graph[y][x][nd] = []
                    fast[y][x][nd] = next[0] + 1000
                if fast[y][x][nd] == next[0] + 1000:
                    graph[y][x][nd].append((y, x, d))
                    heappush(pq, [next[0] + 1000, nd, y, x])
        dy, dx = y + dirs[d][1], x + dirs[d][0]
        if next[0] + 1 <= best and not visited[dy][dx][d] and grid[dy][dx] != '#':
            if (fast[dy][dx][d] == -1 or fast[dy][dx][d] > next[0] + 1):
                graph[dy][dx][nd] = []
                fast[dy][dx][d] = next[0] + 1
            if fast[dy][dx][d] == next[0] + 1:
                graph[dy][dx][d].append((y, x, d))
                heappush(pq, [next[0] + 1, d, dy, dx])
        
        if grid[next[2]][next[3]] == 'E':
            continue
    q = deque()
    visited = [[[False, False, False, False] for i in range(len(grid[0]))] for j in range(len(grid))]
    counter = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(4):
        q.append((ey, ex, i))
    while len(q) > 0:
        next = q.popleft()
        if visited[next[0]][next[1]][next[2]]:
            continue
        counter[next[0]][next[1]] = True
        visited[next[0]][next[1]][next[2]] = True
        for edge in graph[next[0]][next[1]][next[2]]:
            q.append(edge)
    total = sum(i for row in counter for i in row if i)
    print(total)


        
one()
two()