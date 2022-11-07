def has_cycle(head):
    tail = head
    h = head
    while h and h.next:
        tail = tail.next
        h = h.next.next
        if h == tail:
            return 1
    return 0
