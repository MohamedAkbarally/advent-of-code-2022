import math

def is_connected(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])

    if x <= 1 and y <= 1:
        return True
    return False

def get_head_moves(xs):
    head = [0,0]
    head_moves = [(0,0)]

    i = 0
    while i < len(xs):
        cs = xs[i].split(" ")

        for _ in range(int(cs[1])):

            if cs[0] == "U":
                head[1] += 1
            if cs[0] == "D":
                head[1] -= 1
            if cs[0] == "L": 
                head[0] -= 1  
            if cs[0] == "R":
                head[0] += 1

            head_moves.append(tuple(head))
        i+=1

    return head_moves


def get_tail_moves(head_moves):
    tail_moves = [(0,0)]
    for i in range(len(head_moves)):
        if not is_connected(head_moves[i], tail[-1]):
            tail = head_moves[i-1]
        tail_moves.append(tail)

    print(tail_moves)
    return tail_moves


def p1(f):
    xs = f.read().splitlines()
    head_moves = get_head_moves(xs)
    tail_moves = get_tail_moves(head_moves)

    return len(set(tail_moves))

def p2(f):
    xs = f.read().splitlines()

    if len(xs) > 100:
        return
    head_moves = get_head_moves(xs)
    tail_moves = head_moves
    
    
    for i in range(10):
        tail_moves = get_tail_moves(tail_moves)

    return len(set(tail_moves))
