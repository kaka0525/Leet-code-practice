def left_most(root):
    while root.left:
        root = root.left
    return root


def next_in_order_node(node):
    """
    Find the next in order node of given node in binary tree. Write the program
    of same. pointer to parent node is given.
    """
    if node.right is None:
        if node.parent is None or node.parent.right is node:
            return None
        else:
            return node.parent
    else:
        return left_most(node.right)
