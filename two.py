def one():
    with open("two.txt", "r") as read:
        count = 0
        for line in read:
            vals = list(map(int, line.split()))
            good = True
            for i in range(1, len(vals)):
                if vals[i] == vals[i - 1] or (vals[i] > vals[i - 1]) != (vals[1] > vals[0]) or abs(vals[i] - vals[i - 1]) > 3:
                    good = False
                    break
            count += 1 if good else 0
        print(count)

def two():
    with open("two.txt", "r") as read:
        count = 0
        for line in read:
            vals = list(map(int, line.split()))
            temp = vals.copy()
            good = True
            for i in range(len(temp)):
                vals.remove(temp[i])
                good = True
                for j in range(1, len(vals)):
                    if vals[j] == vals[j - 1] or (vals[j] > vals[j - 1]) != (vals[1] > vals[0]) or abs(vals[j] - vals[j - 1]) > 3:
                        good = False
                        break
                if good:
                    break
                vals.insert(i, temp[i])    
            count += 1 if good else 0
        print(count)

one()
two()