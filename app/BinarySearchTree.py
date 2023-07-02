class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, node, new_node):
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_node(node.right, new_node)

    def search(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, node, key):
        while node is not None:
            if key == node.data:
                return node
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return None


def search_word(bst, word):
    node = bst.search(word)
    return node is not None



