def is_connected(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])

    if x <= 1 and y <= 1:
        return True

    if x > 2 or y > 2:
        print("hello")
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
    tail_moves = []
    for i in range(len(head_moves)):
        tail = tail_moves[-1] if len(tail_moves) > 0 else (0,0)
        if not is_connected(head_moves[i],tail):
            new_tail_x = tail[0]
            new_tail_y = tail[1]
            if head_moves[i][0] != tail[0]:
                new_tail_x+= (1 if tail[0] < head_moves[i][0] else -1)
            
            if head_moves[i][1] != tail[1]:
                new_tail_y +=  (1 if tail[1] < head_moves[i][1] else -1)

            tail = (new_tail_x,new_tail_y)
        tail_moves.append(tail)

    return tail_moves


def p1(f):
    xs = f.read().splitlines()
    head_moves = get_head_moves(xs)
    tail_moves = get_tail_moves(head_moves)

    return len(set(tail_moves))

def p2(f):
    xs = f.read().splitlines()

    head_moves = get_head_moves(xs)
    tail_moves = head_moves

    for i in range(9):
        tail_moves = get_tail_moves(tail_moves)
        
    return len(set(tail_moves))
