import networkx as nx

with open("twentythree.txt", "r") as read:
	adj = []
	for line in read:
		adj.append(line.strip().split("-"))

def one():
	graph = {}
	for a, b in adj:
		graph.setdefault(a, []).append(b)
		graph.setdefault(b, []).append(a)
	used = set()
	total = 0
	for comp in graph:
		if comp[0] == "t":
			for i in range(len(graph[comp])):
				for j in range(i + 1, len(graph[comp])):
					if graph[comp][i] not in used and graph[comp][j] not in used and graph[comp][j] in graph[graph[comp][i]]:
						total += 1
			used.add(comp)
	print(total)

def two():
	graph = nx.Graph()
	for a, b in adj:
		graph.add_edge(a, b)
	cliques = list(nx.enumerate_all_cliques(graph))
	best = max(cliques, key=len)
	print(",".join(sorted(best)))
	
one()
two()