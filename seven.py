with open("seven.txt", "r") as read:
	data = [(int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split()))) for line in read]

def solve(res, nums, total, i, concat=False):
	if i == len(nums):
		return total == res
	if total > res:
		return False
	opts = [
		solve(res, nums, total + nums[i], i + 1, concat),
		solve(res, nums, total * nums[i], i + 1, concat)
	]
	if concat:
		opts.append(solve(res, nums, int(f"{total}{nums[i]}"), i + 1, concat))
	return any(opts)

def one():
	print(sum(r for r, n in data if solve(r, n, n[0], 1)))

def two():
	print(sum(r for r, n in data if solve(r, n, n[0], 1, True)))

one()
two()