def p1(f):
    return max([sum([int(x) for x in xs.split("\n")]) for xs in f.read().split("\n\n")])

def p2(f):
    return sum(sorted([sum([int(x) for x in xs.split("\n")]) for xs in f.read().split("\n\n")])[-3:])