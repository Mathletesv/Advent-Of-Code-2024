from functools import cache
from collections import deque

with open("twentyone.txt", "r") as read:
	codes = read.read().split("\n")

num = {
	"0": [("2", "^"), ("A", ">")],
	"1": [("2", ">"), ("4", "^")],
	"2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
	"3": [("2", "<"), ("6", "^"), ("A", "v")],
	"4": [("1", "v"), ("5", ">"), ("7", "^")],
	"5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
	"6": [("3", "v"), ("5", "<"), ("9", "^")],
	"7": [("4", "v"), ("8", ">")],
	"8": [("5", "v"), ("7", "<"), ("9", ">")],
	"9": [("6", "v"), ("8", "<")],
	"A": [("0", "<"), ("3", "^")],
}

dir = {
	"^": [("A", ">"), ("v", "v")],
	"<": [("v", ">")],
	"v": [("<", "<"), ("^", "^"), (">", ">")],
	">": [("v", "<"), ("A", "^")],
	"A": [("^", "<"), (">", "v")],
}
pads = [num, dir]

def bfs(u, v, g):
	q = deque([(u, [])])
	seen = {u}
	shortest = None
	res = []
	while q:
		cur, path = q.popleft()
		if cur == v:
			if shortest is None:
				shortest = len(path)
			if len(path) == shortest:
				res.append("".join(path + ["A"]))
			continue
		if shortest and len(path) >= shortest:
			continue
		for n, d in g[cur]:
			seen.add(n)
			q.append((n, path + [d]))
	return res

@cache
def dfs(seq, level, i=0):
	g = pads[i]
	res = 0
	prev = "A"
	for v in seq:
		paths = bfs(prev, v, g)
		if level == 0:
			res += min(map(len, paths))
		else:
			res += min(dfs(path, level - 1, 1) for path in paths)
		prev = v
	return res

def one():
	total = sum(dfs(code, 2) * int(code[:3]) for code in codes)
	print(total)

def two():
	total = sum(dfs(code, 25) * int(code[:3]) for code in codes)
	print(total)

one()
two()