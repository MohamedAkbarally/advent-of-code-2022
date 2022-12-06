def p1(f):
    xs = f.read()
    return min([i for i in range(4, len(xs)) if len(set(xs[i-4:i])) == 4 ])

def p2(f):
    xs = f.read()
    return min([i for i in range(14, len(xs)) if len(set(xs[i-14:i])) == 14 ])
