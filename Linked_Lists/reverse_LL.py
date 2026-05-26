from Linked_lists import singly_linkedlist

def reverse_LL(head):
    temp = None
    curr = head
    while curr :
        present = curr.next
        curr.next = temp
        temp = curr
        curr = present
    return temp

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
d.next = e

head.display_linkedlist(head)
head = reverse_LL(head)
a.display_linkedlist(head)   #a. or head. does not matter, only the parameter matters

