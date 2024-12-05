after = {}
before = {}
checks = []
with open("five.txt", "r") as read:
	for line in read:
		if line == '\n':
			break
		one, two = map(int, line.split('|'))
		if one not in after:
			after[one] = set()
		after[one].add(two)
		if two not in before:
			before[two] = set()
		before[two].add(one)
	for line in read:
		checks.append(line.strip())

def test(list):
	ind = set(list)
	good = True
	for i in list:
		ind.remove(i)
		if i not in before:
			continue
		for b in before[i]:
			if b in ind:
				return False
	return True


def one():
	total = 0
	for line in checks:
		lis = list(map(int, line.split(',')))
		res = test(lis)
		if res:
			total += lis[int((len(lis) - 1) / 2)]
	print(total)

def fix(list):
	for i in list:
		count = 0
		if not i in before:
			continue
		for j in list:
			if j in before[i]:
				count += 1
		if count == int(len(list) / 2):
			return i

def two():
	total = 0
	for line in checks:
		lis = list(map(int, line.split(',')))
		res = test(lis)
		if not res:
			total += fix(lis)
	print(total)

one()
two()