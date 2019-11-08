class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.insert(value)

    def show(self):
        print(self.value)
        if self.next is not None:
            self.next.show()