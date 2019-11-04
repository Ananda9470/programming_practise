from BST import BST

# O(n) | O(1)
# Θ(log(n)) | O(1)
def findClosestValueInBst1(tree, target):

    closest = float("inf")
    while True:

        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value

        if tree.value > target:
            if tree.left is not None:
                tree = tree.left
            else:
                return closest
        elif tree.value < target:
            if tree.right is not None:
                tree = tree.right
            else:
                return closest
        else:
            return tree.value

# O(n) | O(n)
# Θ(log(n)) | O(log(n)
def findClosestValueInBst2(tree, target):

    def findClosestValueInBstRecussor(tree, target, smallest):

        if tree is None:
            return smallest

        if abs(tree.value - target) < abs(smallest - target):
            smallest = tree.value

        if tree.value > target:
            tree = tree.left
        elif tree.value < target:
            tree = tree.right
        else:
            return smallest

        return findClosestValueInBstRecussor(
            tree,
            target,
            smallest
        )

    return findClosestValueInBstRecussor(tree, target, float("inf"))

if __name__ == "__main__":
    bst = BST(100)
    bst.insert(5)
    bst.insert(6)
    bst.insert(105)
    bst.insert(103)
    bst.insert(1)

    ans = findClosestValueInBst2(bst, 101)
    print(ans)