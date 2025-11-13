import re
with open("/workspaces/Advent2024/Day5/input.txt", "r") as file:
    file = file.read()
    a = file.split('\n\n')
    order = a[0]
    downloads = a[1].split('\n')
def part1():
    times_seen = {}
    relevant_numbers = []
    correct_order = []
    new_order = []
    total = 0
    for i in downloads:
        for j in i.split(','):
            if j not in relevant_numbers:
                relevant_numbers.append(j) 
        for i in relevant_numbers:
            p = re.findall(r'{}[|][0-9]+'.format(i), order)
            p += re.findall(r'[0-9]+[|]{}'.format(i), order)
            for rules in p:
                rules = rules.split('|')
                if all(rule not in new_order for rule in rules):
                    new_order.append('|'.join(rules))
    print(new_order)

part1()