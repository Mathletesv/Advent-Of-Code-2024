import re

with open("fourteen.txt", "r") as read:
	data = read.read().split("\n")

def one():
	quads = [[0, 0], [0, 0]]
	for line in data:
		(px, py, vx, vy) = map(int, re.findall(r"(-?\d+)", line))
		px += vx * 100
		py += vy * 100
		px %= 101
		py %= 103
		if px != 50 and py != 51:
			quads[px // 51][py // 52] += 1
	print(quads[0][0] * quads[1][1] * quads[0][1] * quads[1][0])

def two():
	grid = [[0 for j in range(101)] for i in range(103)]
	robots = []
	for line in data:
		(px, py, vx, vy) = map(int, re.findall(r"(-?\d+)", line))
		robots.append([(px, py), (vx, vy)])
	mcounter = 0
	for t in range(10000):
		rows = [[] for i in range(103)] 
		for r in robots:
			(rx, ry), (vx, vy) = r
			grid[ry][rx] -= 1
			rx = (rx + vx) % 101
			ry = (ry + vy) % 103
			grid[ry][rx] += 1
			rows[ry].append(rx)
			r[0] = (rx, ry)
		counter = 0
		for i in range(103):
			rows[i].sort()
			prev = -1
			counter = 0
			for x in rows[i]:
				if x == prev + 1:
					counter += 1
				elif x > prev + 1:
					counter = 1
				prev = x
				mcounter = max(mcounter, counter)
		if mcounter > 15:
			print(t)
			break
	#print(mcounter)
	# for i in range(103):
	# 	for j in range(101):
	# 		if grid[i][j] > 0:
	# 			print("#", end="")
	# 		else:
	# 			print(" ", end="")
	# 	print()

one()
two()