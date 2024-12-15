with open("fifteen.txt", "r") as read:
	map = []
	while (line := read.readline().strip()) != "":
		map.append(list(line))

	steps = "".join(line.strip() for line in read)

def one():
	grid = []
	for row in map:
		grid.append(row.copy())
	def end(x, y, dir):
		while grid[y][x] != ".":
			x += dir[0]
			y += dir[1]
			if grid[y][x] == "#":
				return (-1, -1)
		return (x, y)
	rx, ry = 0, 0
	for y, row in enumerate(grid):
		for x, char in enumerate(row):
			if char == "@":
				rx, ry = x, y
				break
	dirs = {
		"<": (-1, 0),
		">": (1, 0),
		"^": (0, -1),
		"v": (0, 1),
	}

	for step in steps:
		next_x, next_y = end(rx, ry, dirs[step])
		if next_x != -1 and next_y != -1:
			if step in "<>" and abs(next_x - rx) > 1:
				grid[ry][next_x] = "O"
			elif step in "^v" and abs(next_y - ry) > 1:
				grid[next_y][rx] = "O"
			grid[ry][rx] = "."
			rx, ry = rx + dirs[step][0], ry + dirs[step][1]
			grid[ry][rx] = "@"

	total = sum(100 * i + j for i, row in enumerate(grid) for j, char in enumerate(row) if char == "O")
	print(total)

def two():
	grid = []
	for row in map:
		r = []
		for c in row:
			if c == "@":
				r.extend(["@", "."])
			elif c == "O":
				r.extend(["[", "]"])
			else:
				r.extend([c, c])
		grid.append(r)
	def end_horiz(x, y, dir):
		while grid[y][x] != ".":
			x += dir
			if grid[y][x] == "#":
				return -1
		return x
	def end_vert(x, y, dir):
		if grid[y][x] == '.':
			return True
		elif grid[y][x] == "]":
			return end_vert(x, y + dir, dir) and end_vert(x - 1, y + dir, dir)
		elif grid[y][x] == "[":
			return end_vert(x, y + dir, dir) and end_vert(x + 1, y + dir, dir)
		return False
	def run_vert(x, y, dir, right = False):
		if grid[y][x] == '.':
			return
		elif grid[y][x] == "]" and not right:
			run_vert(x - 1, y, dir)
		elif grid[y][x] == "[":
			run_vert(x + 1, y + dir, dir, True)
			run_vert(x, y + dir, dir)
			grid[y + dir][x] = "["
			grid[y + dir][x + 1] = "]"
			grid[y][x] = "."
			grid[y][x + 1] = "."
	rx, ry = 0, 0
	for y, row in enumerate(grid):
		for x, char in enumerate(row):
			if char == "@":
				rx, ry = x, y
				break
	dirs = {
		"<": (-1, 0),
		">": (1, 0),
		"^": (0, -1),
		"v": (0, 1),
	}
	for step in steps:
		if step in "<>":
			dx = dirs[step][0]
			next_x = end_horiz(rx, ry, dx)
			if next_x != -1:
				while next_x != rx:
					grid[ry][next_x] = grid[ry][next_x - dx]
					next_x -= dx
				grid[ry][rx] = "."
				rx += dx
		else:
			dy = dirs[step][1]
			next_y = ry + dy
			if end_vert(rx, next_y, dy):
				run_vert(rx, next_y, dy)
				grid[ry][rx] = "."
				ry = next_y
				grid[ry][rx] = "@"

	total = sum(100 * i + j for i, row in enumerate(grid) for j, char in enumerate(row) if char == "[")
	print(total)

one()
two()