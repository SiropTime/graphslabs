# Дано N-дерево. Найти все вершины равноудалённые от корня и от ближайшего своего листа

import random


#  Дерево
class Node:
    key: int
    nodes: list

    def __init__(self, key: int, nodes: tuple = ()):
        self.key = key
        self.nodes = list(nodes)


# n - количество вершин в дереве, m - максимальное количество ветвей в уровне
def generate_random_tree(n: int, m: int) -> Node | None:
    if n == 0:
        return None
    nodes = []
    for i in range(random.randint(0, m)):
        nodes.append(generate_random_tree(n - 1, m))
    return Node(random.randint(0, 100), tuple(nodes))


def solution(node: Node) -> list:
    if node is None:
        return []
    if not node.nodes:
        return [node]
    result = []
    for i in node.nodes:
        result += solution(i)
    if len(result) == 1:
        return [node.key]
    return result


if __name__ == "__main__":
    n, m = map(int, input("Введите общее количество вершин дерева и максимальное количество вершин на уровне: ")
               .split())
    tree = generate_random_tree(n, m)
    print(solution(tree))
