from LinkedList import LinkedList

# O(n) | O(1)
def findLoop(head):

    first = head.next
    second = head.next.next

    while first is not second:
        first = first.next
        second = second.next.next
    first = head
    while first is not second:
        first = first.next
        second = second.next

    return first

if __name__ == "__main__":
    ll = LinkedList(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    ll.insert(9)
    ll.next.next.next.next.next.next.next.next.next.next = ll.next.next.next.next

    node = findLoop(ll)
    print(node.value)