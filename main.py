from typing import List, Callable, Any


class BinaryNode:
    """Klasa reprezentujaca wezel drzewa binarnego."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"

    def is_leaf(self):
        return self.left is None and self.right is None

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left:
            self.left.traverse_pre_order(visit)
        if self.right:
            self.right.traverse_pre_order(visit)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left:
            self.left.traverse_in_order(visit)
        visit(self)
        if self.right:
            self.right.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left:
            self.left.traverse_post_order(visit)
        if self.right:
            self.right.traverse_post_order(visit)
        visit(self)


class BinaryTree:
    """ Klasa wrapper przedstawiajaca drzewo binarne na bazie klasy BinaryNode"""

    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)


def all_paths(tree: BinaryTree) -> List[List[BinaryNode]]:
    """ Glowna funkcja zawierajacy liste sciezek drzewa do ktorego dodawane beda poszczegolne elemeny drzewa"""
    output_paths = []
    binary_node = tree.root
    traverse_through_tree(binary_node, output_paths, [])
    return output_paths


def traverse_through_tree(curr_node: BinaryNode, output: List, path: List):
    """Funkcja pomocnicza, ktora przechodzi przez wszystkie wezly i dodaje je do listy output"""
    if curr_node is None:
        return

    if curr_node.is_leaf():
        output.append(path + [curr_node])

    if curr_node.left:
        traverse_through_tree(curr_node.left, output, path + [curr_node])
    if curr_node.right:
        traverse_through_tree(curr_node.right, output, path + [curr_node])


def visit_node(bin_node: BinaryNode):
    print(bin_node.data)


# Stworzenie drzewa podanego w tresci zadania
node = BinaryNode(1)
node.left = BinaryNode(2)
node.right = BinaryNode(3)
node.left.right = BinaryNode(5)
node.left.left = BinaryNode(4)
node.left.left.left = BinaryNode(8)
node.left.left.right = BinaryNode(9)
node.right.right = BinaryNode(7)

# Wydrukowanie otrzymanych sciezek
t = BinaryTree(node)
paths = all_paths(t)
print(paths)
print('####################')
print("Przejscie pre_order")
t.traverse_pre_order(visit_node)
print('####################')
print("Przejscie post_order")
t.traverse_post_order(visit_node)
print('####################')
print("Przejscie in_order")
t.traverse_in_order(visit_node)

# Testowanie drzewa z pojedynczym wezlem o wartosci None
node_2 = BinaryNode(None)
t2 = BinaryTree(node_2)
paths2 = all_paths(t2)
print(paths2)