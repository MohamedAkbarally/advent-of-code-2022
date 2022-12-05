import re

def input_to_arr(f):
    return [list(map(int,re.split(",|-", x))) for x in f.read().split()]

def is_contained(xs,ys):
    sx = set(xs)
    sy = set(ys)
    if sx.issubset(sy) or sy.issubset(sx):
        return True
    return False

def p1(f):
    xs = input_to_arr(f)
    return sum([is_contained(list(range(x[0],x[1]+1)), list(range(x[2],x[3]+1))) for x in xs])

def p2(f):
    xs = input_to_arr(f)
    return sum([not set(range(x[0],x[1]+1)).isdisjoint(set(range(x[2],x[3]+1))) for x in xs])