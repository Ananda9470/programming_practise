class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def contains(self, value):
        if self.value == value:
            return True

        if self.left is not None:
            left_contains = self.left.contains(value)
        else:
            left_contains = False

        if self.right is not None:
            right_contains = self.right.contains(value)
        else:
            right_contains = False

        return left_contains or right_contains

    def remove(self, value):
        return self

if __name__ == "__main__":
    bst = BST(100)
    bst.insert(5)
    bst.insert(6)
    bst.insert(105)
    bst.insert(103)
    bst.insert(1)

    ans = bst.contains(1)
    print(ans)