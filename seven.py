res, nums = [], []
with open("seven.txt", "r") as read:
	for line in read:
		sres, snums = line.split(": ")
		res.append(int(sres))
		nums.append(list(map(int, snums.split(" "))))

def solve(res, nums, total, i):
	if i == len(nums):
		if total == res:
			return True
		return False
	if total > res:
		return False
	return solve(res, nums, total + nums[i], i + 1) or solve(res, nums, total * nums[i], i + 1)

def one():
	count = 0
	for r, n in zip(res, nums):
		count += r if solve(r, n, n[0], 1) else 0
	print(count)

def solve2(res, nums, total, i):
	if i == len(nums):
		if total == res:
			return True
		return False
	if total > res:
		return False
	return solve2(res, nums, total + nums[i], i + 1) or solve2(res, nums, total * nums[i], i + 1) or solve2(res, nums, int(f"{total}{nums[i]}"), i + 1)

def two():
	count = 0
	for r, n in zip(res, nums):
		count += r if solve2(r, n, n[0], 1) else 0
	print(count)

one()
two()