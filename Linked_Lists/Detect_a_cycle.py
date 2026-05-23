from Linked_lists import singly_linkedlist

def detect_cycle(head):
    slow = head
    fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            return True
    return False

head = singly_linkedlist(1)
a = singly_linkedlist(2)
b = singly_linkedlist(3)
c = singly_linkedlist(4)
d = singly_linkedlist(5)
e = singly_linkedlist(6)

head.next = a
a.next = b
b.next = c
c.next = d
d.next = c

print(detect_cycle(head))
