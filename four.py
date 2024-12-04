lines = []
with open("four.txt", "r") as read:
    for line in read:
        line = "ZZZ" + line + "ZZZ"
        if len(lines) == 0:
            temp = "Z" * len(line)
            for i in range(3):
                lines.append(temp)
        lines.append(line)

temp = "Z" * len(lines[0])
for i in range(3):
    lines.append(temp)

def one():
	total = 0
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] != 'X':
				continue
			if lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
				total += 1
			if lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
				total += 1
			if lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
				total += 1
			if lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
				total += 1
			if lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
				total += 1
			if lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
				total += 1
			if lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
				total += 1
			if lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
				total += 1
	print(total)

def two():
	total = 0
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] != 'A':
				continue
			if lines[i - 1][j - 1] == 'M':
				if lines[i + 1][j - 1] == 'M' and lines[i - 1][j + 1] == 'S' and lines[i + 1][j + 1] == 'S':
					total += 1
				if lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'S':
					total += 1
			if lines[i + 1][j + 1] == 'M':
				if lines[i + 1][j - 1] == 'M' and lines[i - 1][j + 1] == 'S' and lines[i - 1][j - 1] == 'S':
					total += 1
				if lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S' and lines[i - 1][j - 1] == 'S':
					total += 1
	print(total)

one()
two()