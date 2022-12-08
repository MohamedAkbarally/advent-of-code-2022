def p1(f):
    count = 0
    xs = f.read().split()
    rows = len(xs)

    for i in range(len(xs)):
        for j in range(len(xs[i])):
            val = xs[i][j]
            right = [x for x in xs[i][j+1:] if x >= val]
            left = [x for x in xs[i][:j] if x >= val]
            down = [xs[t][j] for t in range(i+1,rows) if xs[t][j] >= val]
            up = [xs[t][j] for t in range(0,i) if xs[t][j] >= val]

            if len(up) == 0 or len(down) == 0 or len(left)==0 or len(right)==0:
                count +=1

    return count



def p2(f):
    count = 0
    xs = f.read().split()
    rows = len(xs)
    columns = len(xs[0])

    for i in range(len(xs)):
        for j in range(len(xs[i])):
            val = xs[i][j]

            right_count = 0
            for t in range(j+1,columns):
                right_count +=1
                if xs[i][t] >= val:
                    break
            
            left_count = 0
            for t in reversed(range(0,j)):
                left_count +=1
                if xs[i][t] >= val:
                    break

            up_count = 0
            for t in range(i+1,rows):
                up_count +=1
                if xs[t][j] >= val:
                    break

            down_count = 0
            for t in reversed(range(0,i)):
                down_count +=1
                if xs[t][j] >= val:
                    break
                
            count = max(count, down_count * up_count * right_count * left_count)
            
 
    return count
