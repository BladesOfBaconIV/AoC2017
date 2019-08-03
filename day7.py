from collections import Counter
import re

tree = {}
with open('input.txt') as f:
    for line in f:
        parent, importance, *children = re.findall(r'\w+', line)
        tree[parent] = (int(importance), (children))

possible_roots = set(tree) - {child for _, children in tree.values() for child in children}
root = possible_roots.pop()

def weight_supported(node):
    return tree[node][0] + sum(weight_supported(child) for child in tree[node][1])

def find_bad(node, delta=0):
    total_wts = Counter(map(weight_supported, tree[node][1]))
    if len(total_wts)==1: 
        return node, tree[node][0] + delta
    ((balanced, _), (inbalanced, _)) = total_wts.most_common(2)
    bad = [child for child in tree[node][1] if weight_supported(child)==inbalanced].pop()
    return find_bad(bad, balanced-inbalanced)

# part 2 solution based on u/oantolin solution https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/
print(f'Part 1: {root}, Part 2: {find_bad(root)}')