def p1(f):
    data = f.read().split("\n")
    board_str = "".join([line[1::4] for line in data[:8]])
    moves = [move.replace(" to ",",").replace(" from ",",").replace("move ","").split(",") for move in data[10:]]
    board = (["".join(list(reversed(board_str[i::9]))).strip() for i in range(9)])
    for move in moves:
        crates = "".join(reversed(board[int(move[1])-1][-1*int(move[0]):]))
        board[int(move[1])-1] = board[int(move[1])-1][:-1*int(move[0])]
        board[int(move[2])-1] += crates
    return "".join([stack[-1] for stack in board])

def p2(f):
    data = f.read().split("\n")
    board_str = "".join([line[1::4] for line in data[:8]])
    moves = [move.replace(" to ",",").replace(" from ",",").replace("move ","").split(",") for move in data[10:]]
    board = (["".join(list(reversed(board_str[i::9]))).strip() for i in range(9)])
    
    for move in moves:
        crates = "".join(board[int(move[1])-1][-1*int(move[0]):])
  
        board[int(move[1])-1] = board[int(move[1])-1][:-1*int(move[0])]
        board[int(move[2])-1] += crates
    return "".join([stack[-1] for stack in board])