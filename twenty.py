with open("twenty.txt", "r") as read:
    maze = read.read().split("\n")

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def one():
    grid = [[-1 for i in range(len(maze[0]))] for i in range(len(maze))]
    x, y = -1, -1
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if c == 'S':
                x, y = j, i
    grid[y][x] = 0
    while maze[y][x] != 'E':
        for dir in dirs:
            if maze[y + dir[1]][x + dir[0]] != '#' and grid[y + dir[1]][x + dir[0]] == -1:
                grid[y + dir[1]][x + dir[0]] = grid[y][x] + 1
                y += dir[1]
                x += dir[0]
    total = 0
    for y in range(len(maze)):
        for x in range(len(maze[i])):
            if maze[y][x] != '#':
                for dir in dirs:
                    if 0 < y + dir[1] * 2 < len(grid) and 0 < x + dir[0] * 2 < len(grid[0]) and grid[y + dir[1] * 2][x + dir[0] * 2] - grid[y][x] - 2 >= 100:
                        total += 1
    print(total)

def two():
    grid = [[-1 for i in range(len(maze[0]))] for i in range(len(maze))]
    x, y = -1, -1
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if c == 'S':
                x, y = j, i
    grid[y][x] = 0
    while maze[y][x] != 'E':
        for dir in dirs:
            if maze[y + dir[1]][x + dir[0]] != '#' and grid[y + dir[1]][x + dir[0]] == -1:
                grid[y + dir[1]][x + dir[0]] = grid[y][x] + 1
                y += dir[1]
                x += dir[0]
    total = 0
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] != '#':
                for i in range(-20, 21, 1):
                    for j in range(abs(i) - 20, 21 - abs(i), 1):
                        if 0 < y + i < len(grid) and 0 < x + j < len(grid[0]) and grid[y + i][x + j] - grid[y][x] - abs(i) - abs(j) >= 100:
                            total += 1
    print(total)

one()
two()