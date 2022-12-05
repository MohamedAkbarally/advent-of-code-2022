
def get_priority(c):
    if c.lower() == c:
        return ord(c) - 96
    return ord(c) - 38

def p1(f):
    xs = f.read().split()
    return sum([get_priority(list(set(x[:len(x)//2]) & set(x[len(x)//2:]))[0]) for x in xs])

def p2(f):
    xs = f.read().split()
    return sum([get_priority(list(set(x[0]) & set(x[1]) & set(x[2]))[0]) for x in list(zip(xs,xs[1:],xs[2:]))[::3]])
