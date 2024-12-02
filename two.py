def test(vals):
    good = True
    for i in range(1, len(vals)):
        if vals[i] == vals[i - 1] or (vals[i] > vals[i - 1]) != (vals[1] > vals[0]) or abs(vals[i] - vals[i - 1]) > 3:
            good = False
            break
    return good

def one():
    with open("two.txt", "r") as read:
        count = 0
        for line in read:
            vals = list(map(int, line.split()))
            count += 1 if test(vals) else 0
        print(count)

def two():
    with open("two.txt", "r") as read:
        count = 0
        for line in read:
            vals = list(map(int, line.split()))
            good = test(vals)
            temp = vals.copy()
            for i in range(len(vals)):
                if good:
                    break
                temp.pop(i)
                good = test(temp)
                temp.insert(i, vals[i])
            count += 1 if good else 0
        print(count)

one()
two()