import re

with open("thirteen.txt", "r") as read:
	data = read.read().split("\n\n")

def one():
	total = 0
	for dataset in data:
		lines = dataset.split("\n")
		lines[0] += 'end.'
		lines[1] += 'end.'
		lines[2] += 'end.'
		x1 = int(re.search(r'X+(.*?),', lines[0]).group(1).lstrip('+'))
		x2 = int(re.search(r'X+(.*?),', lines[1]).group(1).lstrip('+'))
		y1 = int(re.search(r'Y+(.*?)end.', lines[0]).group(1).lstrip('+'))
		y2 = int(re.search(r'Y+(.*?)end.', lines[1]).group(1).lstrip('+'))
		rx = int(re.search(r'X=(.*?),', lines[2]).group(1).lstrip('='))
		ry = int(re.search(r'Y=(.*?)end.', lines[2]).group(1).lstrip('='))
		b = (rx / x1 - ry / y1) / (x2 / x1 - y2 / y1)
		a = (rx - x2 * b) / x1
		if abs(round(a) - a) < .001 and abs(round(b) - b) < .001:
			total += round(a) * 3 + round(b)
	print(total)
		

def two():
	total = 0
	for dataset in data:
		lines = dataset.split("\n")
		lines[0] += 'end.'
		lines[1] += 'end.'
		lines[2] += 'end.'
		x1 = int(re.search(r'X+(.*?),', lines[0]).group(1).lstrip('+'))
		x2 = int(re.search(r'X+(.*?),', lines[1]).group(1).lstrip('+'))
		y1 = int(re.search(r'Y+(.*?)end.', lines[0]).group(1).lstrip('+'))
		y2 = int(re.search(r'Y+(.*?)end.', lines[1]).group(1).lstrip('+'))
		rx = int(re.search(r'X=(.*?),', lines[2]).group(1).lstrip('='))
		ry = int(re.search(r'Y=(.*?)end.', lines[2]).group(1).lstrip('='))
		rx += 10000000000000
		ry += 10000000000000
		b = (rx / x1 - ry / y1) / (x2 / x1 - y2 / y1)
		a = (rx - x2 * b) / x1
		if abs(round(a) - a) < .001 and abs(round(b) - b) < .001:
			total += round(a) * 3 + round(b)
	print(total)

one()
two()