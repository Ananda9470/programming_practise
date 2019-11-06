from BST import BST

# O(n) | O(d)
def validateBst(tree):
    return validateBSTRecursor(tree, range_min=float("-inf"), range_max=float("inf"))

def validateBSTRecursor(tree, range_min, range_max):

    if tree is not None:
        good_node = range_min <= tree.value < range_max
        good_l_sub_tree = validateBSTRecursor(tree.left, range_min, tree.value)
        good_r_sub_tree = validateBSTRecursor(tree.right, tree.value, range_max)

        return good_node and good_l_sub_tree and good_r_sub_tree

    else:
        return True

if __name__ == "__main__":

    bst = BST(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    bst.insert(22)
    bst.insert(13)
    bst.insert(14)

    ans = validateBst(bst)
    print(ans)