import ast
from functools import cmp_to_key

def compare(left_input,right_input):

    if len(right_input) == 0 and len(left_input) == 0:
        return 'SAME'

    if len(right_input) == 0:
        return False
    
    if len(left_input) == 0:
        return True

    left = left_input.pop(0)
    right = right_input.pop(0)

    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        if left == right:
            return compare(left_input, right_input)
    
    if type(left) == list and type(right) == list:
        output = compare(left, right)

        if output == 'SAME':
            return compare(left_input, right_input)
        else:
            return output

    if type(left) == int and type(right) == list:
        output = compare([left], right)

        if output == 'SAME':
            return compare(left_input, right_input)
        else:
            return output
            
    if type(left) == list and type(right) == int:
        output = compare(left, [right])

        if output == 'SAME':
            return compare(left_input, right_input)
        else:
            return output

def parse_arr(str):
    return ast.literal_eval(str)


def p1(f):
    pairs = f.read().split("\n\n")
    indices = []
    for i, pair in enumerate(pairs):
        left_input, right_input = tuple(pair.splitlines())
        if (compare(parse_arr(left_input), parse_arr(right_input)) == 'SAME'):
            print("hello")

        if (compare(parse_arr(left_input), parse_arr(right_input)) == True):
            indices.append(i+1)

    return sum(indices)


def sort_compare(item1, item2):
    output = compare(parse_arr(item1), parse_arr(item2))

    if output == 'SAME':
        return 0

    if output == True:
        return -1

    if output == False:
        return 1

def p2(f):
    pairs = f.read().replace("\n\n","\n").splitlines()
    pairs += ["[[2]]","[[6]]"]
    sorted_pairs = sorted(pairs, key=cmp_to_key(sort_compare))
    return (sorted_pairs.index("[[2]]")+1) * (sorted_pairs.index("[[6]]")+1)