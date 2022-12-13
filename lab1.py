import random


class Node:
    def __init__(self, key: int, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# function that finds max branching in binary tree
def find_max_branching_by_len(node: Node, max_branching: int = 0) -> int:
    if not node:
        return max_branching

    return max(find_max_branching_by_len(node.left, max_branching+1),
               find_max_branching_by_len(node.right, max_branching+1))


def generate_random_tree(n: int) -> Node | None:
    if n == 0:
        return None
    nodes = []
    for i in range(random.randint(0, 2)):
        nodes.append(generate_random_tree(n - 1))
    return Node(random.randint(0, 100), *nodes)


def print_tree(node: Node, level: int = 0) -> None:
    if not node:
        return
    print(" " * level, node.key)
    for i in (node.left, node.right):
        print_tree(i, level + 1)


if __name__ == '__main__':
    n = int(input("Введите количество вершин в дереве: "))
    tree = generate_random_tree(n)
    print(find_max_branching_by_len(tree))
