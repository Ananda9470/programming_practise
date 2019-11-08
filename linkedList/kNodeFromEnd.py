from LinkedList import LinkedList

# O(n) | O(1)
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter<=k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    else:
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = first.next.next

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

    removeKthNodeFromEnd(ll, 10)
    ll.show()