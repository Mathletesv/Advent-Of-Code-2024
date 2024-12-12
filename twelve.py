with open("twelve.txt", "r") as read:
	data = read.read().split()

def one():
	total = 0
	reached = [[False for j in range(len(data[0]))] for i in range(len(data))]
	def flood(i, j, v):
		if i < 0 or i >= len(data) or j < 0 or j >= len(data[i]) or data[i][j] != v:
			return (1, 0)
		if reached[i][j]:
			return (0, 0)
		reached[i][j] = True
		tp, ta = 0, 1
		for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			(p, a) = flood(i + di, j + dj, v)
			tp += p
			ta += a
		return (tp, ta)

	for i in range(len(data)):
		for j in range(len(data[i])):
			if reached[i][j]:
				continue
			(p, a) = flood(i, j, data[i][j])
			total += p * a
	print(total)

def two():
	total = 0
	reached = [[False for j in range(len(data[0]))] for i in range(len(data))]
	def flood(i, j, v, d):
		if i < 0 or i >= len(data) or j < 0 or j >= len(data[i]) or data[i][j] != v:
			return ([(f"{i}a{d[0]}", f"{j}a{d[1]}")], 0)
		if reached[i][j]:
			return ([], 0)
		reached[i][j] = True
		tp, ta = [], 1
		for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			(p, a) = flood(i + di, j + dj, v, (di, dj))
			tp.extend(p)
			ta += a
		return (tp, ta)
	
	def get_pair(i, j, a):
		if a:
			return (j, i)
		else:
			return (i, j)

	for i in range(len(data)):
		for j in range(len(data[i])):
			if reached[i][j]:
				continue
			(p, area) = flood(i, j, data[i][j], (0, 0))
			np = p.copy()
			for v in p:
				if v not in np:
					continue
				if v[0][-1] == "0":
					a, b = 0, 1
				else:
					a, b = 1, 0
				vs = v[a].split("a")
				tv = int(vs[0]) - 1
				while get_pair(f"{tv}a{vs[1]}", v[b], a) in p:
					np.remove(get_pair(f"{tv}a{vs[1]}", v[b], a))
					tv -= 1
				tv = int(vs[0]) + 1
				while get_pair(f"{tv}a{vs[1]}", v[b], a) in p:
					np.remove(get_pair(f"{tv}a{vs[1]}", v[b], a))
					tv += 1
			total += len(np) * area
	print(total)

one()
two()