import re

graph = {}
with open('input.txt') as f:
    for line in f:
        parent, *children = map(int, re.findall(r'\d+', line))
        graph[parent] = (children)

def find_all_connected(node, seen):
    if node in seen:
        return
    seen.add(node)
    for connected in graph[node]:
        find_all_connected(connected, seen)
    return seen

groups = [find_all_connected(0, set())]
not_seen = set(graph) - groups[0]
while not_seen:
    g = find_all_connected(not_seen.pop(), set())
    groups.append(g)
    not_seen -= g

print(f'Part 1: {len(groups[0])}, Part 2: {len(groups)}')
