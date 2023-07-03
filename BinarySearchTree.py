class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self,node, key):
        return self._search_node(node, key)

    def _search_node(self, node, key):
        while node is not None:
            if key == node.data:
                return node
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return None

def insert(root, data):
    if root is None:
        return BinarySearchTree(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def create_binary_search_tree(sorted_list, start, end):
    if start > end:
        return None
    middle_index = (start + end) // 2
    root = BinarySearchTree(sorted_list[middle_index])
    root.left = create_binary_search_tree(sorted_list, start, middle_index - 1)
    root.right = create_binary_search_tree(sorted_list, middle_index + 1, end)
    return root

def search_word(bst, word):
    node = bst.search(bst,word)
    return node is not None




