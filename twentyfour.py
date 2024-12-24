with open("twentyfour.txt", "r") as read:
	data = read.read().split("\n\n")
	input = data[0].split("\n")
	gates = data[1].split("\n")
	
def one():
	edges = {}
	counts = {}
	for g in gates:
		g = g.split(" ")
		if g[0] not in edges:
			edges[g[0]] = []
		if g[2] not in edges:
			edges[g[2]] = []
		edges[g[0]].append(g[4])
		edges[g[2]].append(g[4])
		counts[g[4]] = (-1, g[1])
	values = {}
	stack = []
	for i in input:
		var, val = i.split(": ")
		val = int(val)
		values[var] = val
		for e in edges[var]:
			if counts[e][0] == -1:
				counts[e] = (val, counts[e][1])
				continue
			v = counts[e][0]
			if counts[e][1] == "AND":
				counts[e] = (v & val, counts[e][1])
			elif counts[e][1] == "OR":
				counts[e] = (v | val, counts[e][1])
			else:
				counts[e] = (v ^ val, counts[e][1])
			stack.append(e)
	while stack:
		e = stack.pop()
		if e not in edges:
			continue
		for v in edges[e]:
			if counts[v][0] == -1:
				counts[v] = (counts[e][0], counts[v][1])
				continue
			if counts[v][1] == "AND":
				counts[v] = (counts[v][0] & counts[e][0], counts[v][1])
			elif counts[v][1] == "OR":
				counts[v] = (counts[v][0] | counts[e][0], counts[v][1])
			else:
				counts[v] = (counts[v][0] ^ counts[e][0], counts[v][1])
			stack.append(v)
	num = 0
	for key in counts:
		if key[0] == "z" and counts[key][0] == 1:
			num += 2 ** int(key[1:])
	print(num)

def two():
	# done by hand i'm lazy
	pass

one()
two()