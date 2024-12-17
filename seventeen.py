import re

with open("seventeen.txt", "r") as read:
    lines = read.readlines()
    ga = re.findall(r'\d+', lines[0])[0]
    gb = re.findall(r'\d+', lines[1])[0]
    gc = re.findall(r'\d+', lines[2])[0]
    gprog = list(map(int, re.findall(r'\d+', lines[4])))

def combo(v, a, b, c):
    if v < 4:
        return v
    elif v == 4:
        return a
    elif v == 5:
        return b
    else:
        return c

def one():
    a, b, c, prog = int(ga), int(gb), int(gc), gprog

    i = 0
    res = []
    while i < len(prog):
        if prog[i] == 0:
            a = a // (2 ** combo(prog[i + 1], a, b, c))
        elif prog[i] == 1:
            b = b ^ prog[i + 1]
        elif prog[i] == 2:
            b = combo(prog[i + 1], a, b, c) % 8
        elif prog[i] == 3:
            if a != 0:
                i = prog[i + 1] - 2
        elif prog[i] == 4:
            b = b ^ c
        elif prog[i] == 5:
            res.append(combo(prog[i + 1], a, b, c) % 8)
        elif prog[i] == 6:
            b = a // (2 ** combo(prog[i + 1], a, b, c))
        elif prog[i] == 7:
            c = a // (2 ** combo(prog[i + 1], a, b, c))
        
        i += 2
    print(",".join(str(v) for v in res))

def dfs(res, prog, step):
    for test in range(8):
        i = 0
        a, b, c = res * 8 + test, 0, 0
        while i < len(prog):
            if prog[i] == 0:
                a = a // (2 ** combo(prog[i + 1], a, b, c))
            elif prog[i] == 1:
                b = b ^ prog[i + 1]
            elif prog[i] == 2:
                b = combo(prog[i + 1], a, b, c) % 8
            elif prog[i] == 3:
                break
            elif prog[i] == 4:
                b = b ^ c
            elif prog[i] == 5:
                if combo(prog[i + 1], a, b, c) % 8 == prog[step]:
                    if step == 0:
                        return res * 8 + test
                    tres = dfs(res * 8 + test, prog, step - 1)
                    if tres > -1:
                        return tres
            elif prog[i] == 6:
                b = a // (2 ** combo(prog[i + 1], a, b, c))
            elif prog[i] == 7:
                c = a // (2 ** combo(prog[i + 1], a, b, c))
            i += 2
    return -1

def two():
    res = dfs(0, gprog, len(gprog) - 1)
    print(res)

one()
two()