DRAW_POINTS = 3
LOSE_POINTS = 0
WINNING_POINTS = 6

def p1(f):
    symbol_points = {'X':1, 'Y':2, 'Z':3}

    def get_score(op, me):
        score = symbol_points[me]
        
        if (op,me) in [('A','X'), ('B','Y'), ('C','Z')]:
            return score + DRAW_POINTS
            
        if (op, me) in [('B','X'), ('C','Y'), ('A','Z')]:
            return score + LOSE_POINTS
            
        return score + WINNING_POINTS

    return sum([get_score(*tuple(x.split(" "))) for x in f.read().split("\n")])


def p2(f):
    winning_points = {'X':LOSE_POINTS, 'Y': DRAW_POINTS, 'Z': WINNING_POINTS }
    symbol_index = {'A':0, 'B':1 , 'C':2 }

    def get_score(op, me):
        score = winning_points[me]
        
        if me == 'Y':
            return score + symbol_index[op] + 1
            
        if me == 'Z':
            return score + ((symbol_index[op]+1)%3) + 1
            
        return score + ((symbol_index[op]-1)%3) + 1

    return sum([get_score(*tuple(x.split(" "))) for x in f.read().split("\n")])