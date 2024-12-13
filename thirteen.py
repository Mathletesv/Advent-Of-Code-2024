import re

with open("thirteen.txt", "r") as read:
	data = read.read().split("\n\n")

def parse(dataset):
	return list(map(int, re.findall(r"[XY][+=](\d+)", dataset)))

def solve_sys(v):
	b = (v[4] / v[0] - v[5] / v[1]) / (v[2] / v[0] - v[3] / v[1])
	a = (v[4] - v[2] * b) / v[0]
	if abs(round(a) - a) < .001 and abs(round(b) - b) < .001:
		return round(a) * 3 + round(b)
	return 0

def one():
	total = 0
	for dataset in data:
		v = parse(dataset)
		total += solve_sys(v)
	print(total)
		

def two():
	total = 0
	for dataset in data:
		v = parse(dataset)
		v[4] += 10000000000000
		v[5] += 10000000000000
		total += solve_sys(v)
	print(total)

one()
two()