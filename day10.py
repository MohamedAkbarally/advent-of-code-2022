   
def p1(f):

    ys = f.read().splitlines()
    xs = [1]

    i = 0
    while i < len(ys):
        x = xs[-1]
        instructions = ys[i].split(" ")
        if instructions[0] == "addx":
            xs += [x,x+int(instructions[1])]
        if instructions[0] == "noop":
            xs += [x]
        i+=1
    
    return sum([xs[i-1]*i for i in [20,60,100,140,180,220]])

def p2(f):
    ys = f.read().splitlines()
    xs = [1]

    i = 0
    while i < len(ys):
        x = xs[-1]
        instructions = ys[i].split(" ")
        if instructions[0] == "addx":
            xs += [x,x+int(instructions[1])]
        if instructions[0] == "noop":
            xs += [x]
        i+=1

    drawing = list(' '*240)
    for i in range(240):
        if xs[i]-1 <= (i%40) <= xs[i]+1:
            drawing[i] = '#'

    print()
    [print(''.join(drawing[i:i+40])) for i in range(0, len(drawing), 40)]
    return 'Done'