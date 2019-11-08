from LinkedList import LinkedList

# O(n) | O(1)
def reverseLinkedList(head):

    first = head
    second = first.next

    if second is None:
        return head

    first.next = None
    third = second.next

    while third is not None:
        second.next = first

        first = second
        second = third
        third = second.next

    second.next = first
    return second

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

    ll = reverseLinkedList(ll)
    ll.show()

