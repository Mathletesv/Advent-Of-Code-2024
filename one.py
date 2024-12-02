read = open("one.txt", "r")
ones = []
twos = []
while next_line := read.readline():
    [one, two] = next_line.split()
    ones.append(int(one))
    twos.append(int(two))
ones.sort()
twos.sort()

def one():
    sum = 0
    for i in range(len(ones)):
        sum += abs(ones[i] - twos[i])
    print(sum)

def two():
    sum = 0
    for i in range(len(ones)):
        sum += ones[i] * twos.count(ones[i])
    print(sum)

one()
two()