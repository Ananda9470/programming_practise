class Node:
    def __init__(self, name, ancestor):
        self.name = name
        self.ancestor = ancestor

# O(d) | O(1)
def getYoungestCommonAncestor1(topAncestor, descendantOne, descendantTwo):

    count1 = 0
    ancestor_d1  = descendantOne
    while True:
        if ancestor_d1 == topAncestor:
            break
        ancestor_d1 = ancestor_d1.ancestor
        count1 += 1

    count2 = 0
    ancestor_d2  = descendantTwo
    while True:
        if ancestor_d2 == topAncestor:
            break
        ancestor_d2 = ancestor_d2.ancestor
        count2 += 1

    diff = abs(count1 - count2)
    if count1 <= count2:
        lower_node = descendantTwo
        upper_node = descendantOne
    else:
        lower_node = descendantOne
        upper_node = descendantTwo

    for _ in range(diff):
        lower_node = lower_node.ancestor

    while lower_node!=upper_node:
        lower_node = lower_node.ancestor
        upper_node = upper_node.ancestor

    return lower_node


# O(d) | O(d)
def getYoungestCommonAncestor2(topAncestor, descendantOne, descendantTwo):

    ancestor_d1  = descendantOne
    ancestor_set ={ancestor_d1.name}
    while True:
        if ancestor_d1 == topAncestor:
            break
        ancestor_d1 = ancestor_d1.ancestor
        ancestor_set.add(ancestor_d1.name)

    ancestor_d2 = descendantTwo
    while True:
        if ancestor_d2.name in ancestor_set:
            return ancestor_d2
        ancestor_d2 = ancestor_d2.ancestor

if __name__ == "__main__":
    A = Node("A", None)

    B = Node("B", A)
    C = Node("C", A)

    D = Node("D", B)
    E = Node("E", B)

    F = Node("F", C)
    G = Node("G", C)

    H = Node("H", D)
    I = Node("I", D)

    # ans = getYoungestCommonAncestor1(A, G, F)
    ans = getYoungestCommonAncestor1(A, A, G)
    print(ans.name)

