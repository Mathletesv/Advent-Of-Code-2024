with open("nineteen.txt", "r") as read:
    data = read.read().split("\n\n")
    twls = set(data[0].split(", "))
    desired = data[1].split("\n")

def one():
    total = 0
    for des in desired:
        possible = {0}
        for i in range(len(des)):
            if any(des[j:i + 1] in twls for j in possible):
                possible.add(i + 1)
        total += len(des) in possible
    print(total)

def two():
    total = 0
    for des in desired:
        ways = [0] * (len(des) + 1)
        ways[0] = 1
        for i in range(len(des)):
            ways[i + 1] += sum(
                ways[j]
                for j in range(i + 1)
                if des[j:i + 1] in twls
            )
        total += ways[len(des)]
    print(total)

one()
two()