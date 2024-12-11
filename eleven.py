with open("eleven.txt", "r") as read:
    data = list(map(int, read.read().split()))

def one():
    def count(val, blinks):
        if blinks == 0:
            return 1
        s = str(val)
        if len(s) % 2 == 0:
            return count(int(s[:len(s) // 2]), blinks - 1) + count(int(s[len(s) // 2:]), blinks - 1)
        if val == 0:
            return count(1, blinks - 1)
        return count(val * 2024, blinks - 1)

    total = sum(count(val, 25) for val in data)
    print(total)

def two():
    mem = {}
    def blink(val):
        if val == "0":
            return ["1"]
        if len(val) % 2 == 0:
            return [val[:len(val) // 2], val[len(val) // 2:]]
        return [str(int(val) * 2024)]
    
    def count(vals, blinks):
        if blinks == 0:
            return len(vals)
        ans = 0
        for v in vals:
            v = v.lstrip("0")
            if v == "":
                v = "0"
            if (v, blinks) not in mem:
                vs = blink(v)
                mem[(v, blinks)] = count(vs, blinks - 1)
            ans += mem[(v, blinks)]
        return ans
    total = count(list(map(str, data)), 75)
    print(total)

one()
two()