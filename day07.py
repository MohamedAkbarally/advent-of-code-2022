
class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.size = None
     
    def get_size(self):
        self.size = sum([child.get_size() for child in self.children.values()])
        return self.size

    def get_all_child_dirs(self):
        child_nodes = []
        for child in self.children.values():
            if type(child) == Dir:
                child_nodes += child.get_all_child_dirs()

        return [self] + child_nodes
        
class File:
    def __init__(self, size):
        self.size = size
    
    def get_size(self):
        return self.size

def find_folder_sizes(node):
    folder_size = 0
    folder_sizes = []
    for child in node.children.values():
        if type(child) == File:
            folder_size += child.size
        else:
            child_folder_sizes = find_folder_sizes(child) 
            folder_sizes += child_folder_sizes
            folder_size += sum(child_folder_sizes)

    return [folder_size] + folder_sizes


def create_tree(xs):
    root = Dir(None)
    currentNode = root

    i = 0
    while i < len(xs):
        cs = xs[i].split(" ")
        i += 1
        if cs[0] == "$":
            if cs[1] == "cd":
                if cs[2] == "/":
                    currentNode = root
                elif cs[2] == "..":
                    currentNode = currentNode.parent
                else:
                    if cs[2] not in currentNode.children:
                            currentNode.children[cs[2]] = Dir(currentNode)
                    currentNode = currentNode.children[cs[2]]
            if cs[1] == "ls":
                ds = xs[i].split(" ")
                while i < len(xs) and xs[i].split(" ")[0] != '$':
                    ds = xs[i].split(" ")
                    if ds[0] == "dir":
                        if ds[1] not in currentNode.children:
                            currentNode.children[ds[1]] = Dir(currentNode)
                    else:
                        currentNode.children[ds[1]] = File(int(ds[0]))
                    i += 1
    return root

def p1(f):
    xs = f.read().splitlines()
    root = create_tree(xs)
    root.get_size()
    return sum([dir.size for dir in root.get_all_child_dirs() if dir.size < 100000])

def p2(f):
    xs = f.read().splitlines()
    root = create_tree(xs)
    root.get_size()
    avaliable_space = (70000000 - root.size)
    space_needed = 30000000 - avaliable_space

    return min([dir.size for dir in root.get_all_child_dirs() if dir.size > space_needed])
