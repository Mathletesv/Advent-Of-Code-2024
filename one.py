ones, twos = [], []
with open("one.txt", "r") as read:
	for line in read:
		one, two = map(int, line.split())
		ones.append(one)
		twos.append(two)
ones.sort()
twos.sort()

def one():
    print(sum(abs(one - two) for one, two in zip(ones, twos)))

def two():
    print(sum(one * twos.count(one) for one in ones))

one()
two()