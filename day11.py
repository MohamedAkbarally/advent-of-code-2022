class Monkey:
    def __init__(self, spec_str):
        spec = spec_str.splitlines()
        self.inspections = 0
        self.items = [int(s) for s in spec[1][18:].split(", ")]
        self.operation_formula = (tuple(spec[2][19:].split(" ")))
        self.diviser = int(spec[3].split(" ")[-1])
        self.true_monkey_num = int(spec[4].split(" ")[-1])
        self.false_monkey_num = int(spec[5].split(" ")[-1])

    def operation(self, old):
        a, operator, b = self.operation_formula
        parse_var = lambda x: old if x == 'old' else int(x)

        a = parse_var(a)
        b = parse_var(b)

        if operator == '*':
            return a * b
        if operator == '+':
            return a + b

    def operation(self, old):
        a, operator, b = self.operation_formula
        parse_var = lambda x: old if x == 'old' else int(x)

        a = parse_var(a)
        b = parse_var(b)

        if operator == '*':
            return (a*b)%19
        if operator == '+':
            return a + b
    
    def handle_item(self):
        self.inspections += 1
    
        item = self.operation(self.items.pop(0))

        if item%self.diviser == 0:
            return self.true_monkey_num, item
        return self.false_monkey_num, item


def p1(f):
    return
    xs = f.read().split("\n\n")
    monkeys = [Monkey(x) for x in xs]
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey_num, item = monkey.handle_item()
                monkeys[monkey_num].items.append(item)
    
    inspections = sorted([m.inspections for m in monkeys])
    print(inspections[-1]*inspections[-2])

def p2(f):
    xs = f.read().split("\n\n")
    monkeys = [Monkey(x) for x in xs]
    inspections = [0]* len(monkeys)

    for i in range(10000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey_num, item = monkey.handle_item()
                monkeys[monkey_num].items.append(item)

        if i == 19:
            print(sorted([m.inspections for m in monkeys]))

    inspections = sorted([m.inspections for m in monkeys])
    print(inspections)
    print(inspections[-1]*inspections[-2])

