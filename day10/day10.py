def print_map(map):
    for line in map:
        print(line)

class Node:
    def __init__(self, value, map, position):
        self.value = value
        self.map = map
        self.position = position
        self.children = []
    
    def __str__(self):
        return self._print_recursive(0)
    
    def _print_recursive(self, level):
        indent = "  " * level
        result = f"{indent}{self.value}: {self.position}\n"
        for child in self.children:
            result += child._print_recursive(level + 1)
        return result
    
    def add_children(self, potential_children):
        for item in potential_children:
            if self.map[item[0]][item[1]] == self.value + 1:
                child = Node(self.value + 1, map=self.map, position=item)
                self.children.append(child)
                make_tree(item, self.map, child)

    def get_leaves(self):
        if not self.children:  # If no children, it's a leaf
            return [self]
        leaves = []
        for child in self.children:
            leaves.extend(child.get_leaves())  # Collect leaves recursively
        return leaves


def make_tree(trailhead, map, root=None):
    if root is None:
        root = Node(map[trailhead[0]][trailhead[1]], map, trailhead)

    potential_children = []
    if trailhead[0] > 0:
        potential_children.append((trailhead[0] - 1, trailhead[1]))
    if trailhead[0] < len(map) - 1:
        potential_children.append((trailhead[0] + 1, trailhead[1]))
    if trailhead[1] > 0:
        potential_children.append((trailhead[0], trailhead[1] - 1))
    if trailhead[1] < len(map[0]) - 1:
        potential_children.append((trailhead[0], trailhead[1] + 1))

    root.add_children(potential_children)
    return root



def part1():
    f = open("input.txt", "r")
    lines = f.readlines()

    map = []

    trailhead_positions = []
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        map.append(lines[i])
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
            if lines[i][j] == 0:
                trailhead_positions.append((i, j))

    print_map(map)
    print(trailhead_positions)

    result = 0
    for trailhead in trailhead_positions:
        root = make_tree(trailhead, map)
        positions = set()
        for leave in root.get_leaves():
            if map[leave.position[0]][leave.position[1]] == 9:
                positions.add(leave.position)
        result += len(positions)

    print(result)
part1()