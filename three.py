text = ""
with open("three.txt", "r") as read:
	for line in read:
		text += line
text += "buffer text"

def one():
	total = 0
	for i in range(len(text) - 10):
		if text[i:i+4] != "mul(":
			continue
		first = ""
		i += 4
		while text[i].isdigit():
			first += text[i]
			i += 1
		if text[i] != ",":
			continue
		second = ""
		i += 1
		while text[i].isdigit():
			second += text[i]
			i += 1
		if text[i] != ")":
			continue
		total += int(first) * int(second)
	print(total)

	

def two():
	total = 0
	do = True
	for i in range(len(text) - 10):
		if text[i:i+4] == "do()":
			do = True
		elif text[i:i+7] == "don't()":
			do = False
		if not do or text[i:i+4] != "mul(":
			continue
		first = ""
		i += 4
		while text[i].isdigit():
			first += text[i]
			i += 1
		if text[i] != ",":
			continue
		second = ""
		i += 1
		while text[i].isdigit():
			second += text[i]
			i += 1
		if text[i] != ")":
			continue
		total += int(first) * int(second)
	print(total)

one()
two()