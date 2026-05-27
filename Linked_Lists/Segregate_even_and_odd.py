from Linked_lists import singly_linkedlist

def segregate_even_and_odd(head):
    even = []
    odd = []
    curr = head
    while curr :
        if curr.val % 2 == 0 :
            even.append(curr.val)
        else :
            odd.append(curr.val)
        curr = curr.next

    full_list = even + odd
    segregated = singly_linkedlist(full_list[0])
    temp = segregated
    for i in full_list[1:] : 
        curr = singly_linkedlist(i)
        temp.next = curr
        temp = temp.next
    return segregated


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
head = segregate_even_and_odd(head)
head.display_linkedlist(head)