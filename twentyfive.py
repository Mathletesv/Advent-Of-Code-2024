with open("twentyfive.txt", "r") as read:
    chunks = read.read().split("\n\n")
    keys, locks = [], []
    for chunk in chunks:
        lines = [list(line) for line in chunk.split("\n")]
        lines = list(zip(*lines))
        heights = [lines[i].count("#") for i in range(len(lines))]
        if lines[0][0] == "#":
            locks.append(heights)
        else:
            keys.append(heights)

def one():
    total = 0
    for lock in locks:
        for key in keys:
            if all(lock[i] + key[i] <= 7 for i in range(5)):
                total += 1
    print(total)

one()