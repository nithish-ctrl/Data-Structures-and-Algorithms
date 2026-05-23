from Linked_lists import singly_linkedlist

def Remove_nth(head,n):
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next 


'''
head = singly_linkedlist(1)
a = singly_linkedlist(2)
b = singly_linkedlist(3)
c = singly_linkedlist(4)
d = singly_linkedlist(5)
e = singly_linkedlist(6)
f = singly_linkedlist(7)
g = singly_linkedlist(8)


head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head.display_linkedlist(head)
Remove_nth(head,4)
head.display_linkedlist(head)

'''
