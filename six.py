import copy

grid = []
with open("six.txt", "r") as read:
	grid = [line.strip() + "z" for line in read]
grid.append("z" * len(grid[0]))
gr = -1
gc = -1
dirs = [(-1, 0),(0, 1),(1, 0),(0, -1)]
dir = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            gr = i
            gc = j
            grid[i] = grid[i].replace("^", ".")

def try_path():
    ends = set()
    visited = []
    visited.append((gr, gc))
    i = gr
    j = gc
    d = dir
    while True:
        r, c = dirs[d]
        while grid[i + r][j + c] == '.':
            i += r
            j += c
            visited.append((i, j))
        if grid[i + r][j + c] == 'z':
            break

        end = (i, j, d)
        if end in ends:
            return None, True
        ends.add(end)
        d = (d + 1) % 4
    return set(visited), False

def one():
    visited, _ = try_path()
    print(len(visited))

def two():
    visited, _ = try_path()
    total = 0
    for r, c in visited:
        orig = grid[r]
        grid[r] = "".join("#" if i == c else ch for i, ch in enumerate(grid[r]))
        _, test = try_path()
        total += test
        grid[r] = orig
    print(total)


one()
two()