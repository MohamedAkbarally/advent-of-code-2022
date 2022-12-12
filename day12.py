alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_value(c):
    if c == 'S':
        return 0
    if c == 'E':
        return len(alphabet) - 1
    return alphabet.index(c)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        if get_value(child.value) - 1 <= get_value(self.value):
            self.children.append(child)

def p1(f):
    xs = f.read().splitlines()
    nodes = [[Node(c) for c in x] for x in xs]
    starting_node = None
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            print
            if nodes[i][j].value == 'S':
                starting_node = nodes[i][j]

            if not  (i - 1 < 0):
                nodes[i][j].add_child(nodes[i-1][j])

            if not  (j - 1 < 0):
                nodes[i][j].add_child(nodes[i][j-1])

            if not  (i + 1 >= len(nodes)):
                nodes[i][j].add_child(nodes[i+1][j])

            if not  (j + 1 >= len(nodes[i])):
                nodes[i][j].add_child(nodes[i][j+1])
        
    i = 0
    current_nodes = [starting_node]
    visited_nodes = [starting_node]

    for i in range(2000):
        new_nodes = []
        for node in current_nodes:
            if node.value == 'E':
                return i
            temp = [child for child in node.children if child not in visited_nodes]
            new_nodes += temp
            visited_nodes += temp
        current_nodes = new_nodes

def p2(f):
    xs = f.read().splitlines()
    nodes = [[Node(c) for c in x] for x in xs]
    starting_nodes = []
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            print
            if nodes[i][j].value == 'S' or nodes[i][j].value == 'a':
                starting_nodes.append(nodes[i][j])

            if not  (i - 1 < 0):
                nodes[i][j].add_child(nodes[i-1][j])

            if not  (j - 1 < 0):
                nodes[i][j].add_child(nodes[i][j-1])

            if not  (i + 1 >= len(nodes)):
                nodes[i][j].add_child(nodes[i+1][j])

            if not  (j + 1 >= len(nodes[i])):
                nodes[i][j].add_child(nodes[i][j+1])
        
    i = 0
    current_nodes = starting_nodes
    visited_nodes = starting_nodes.copy()

    for i in range(2000):
        new_nodes = []
        for node in current_nodes:
            if node.value == 'E':
                return i
            temp = [child for child in node.children if child not in visited_nodes]
            new_nodes += temp
            visited_nodes += temp

        current_nodes = new_nodes
