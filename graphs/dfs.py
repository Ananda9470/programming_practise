class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) | O(v)
    def depthFirstSearch(self, array):

        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array


if __name__ == "__main__":
    node = Node(0)
    node.addChild(1)
    node.children[0].addChild(11)
    node.children[0].addChild(12)
    node.children[0].addChild(13)
    node.children[0].addChild(14)
    node.addChild(2)
    node.children[1].addChild(21)
    node.children[1].addChild(22)
    node.children[1].addChild(23)
    node.children[1].addChild(24)
    node.addChild(3)
    node.children[2].addChild(31)
    node.children[2].addChild(32)
    node.children[2].addChild(33)
    node.children[2].addChild(34)

    names = node.depthFirstSearch(array = [])
    print(names)