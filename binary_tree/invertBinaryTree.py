class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) | O(d)
def invertBinaryTree(tree):

    if tree.left is not None:
        invertBinaryTree(tree.left)
    if tree.right is not None:
        invertBinaryTree(tree.right)

    tree.right, tree.left = tree.left, tree.right

    return tree


if __name__ == "__main__":
    bt = BinaryTree(100)

    bt.left = BinaryTree(5)
    bt.right = BinaryTree(105)

    bt.left.left = BinaryTree(1)
    bt.left.right = BinaryTree(2)
    bt.right.left = BinaryTree(102)
    bt.right.right = BinaryTree(104)

    ans = invertBinaryTree(tree=bt)
    print(ans)

