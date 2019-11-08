from BST import BST

# O(n) | O(n)
def inOrderTraverse(tree, array):

    if tree is not None:

        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

        return array
    else:
        return []

# O(n) | O(n)
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
        return array
    else:
        return []

# O(n) | O(n)
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
        return array
    else:
        return []

if __name__ == "__main__":

    bst = BST(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    bst.insert(22)

    ans = postOrderTraverse(bst, [])

    print(ans)