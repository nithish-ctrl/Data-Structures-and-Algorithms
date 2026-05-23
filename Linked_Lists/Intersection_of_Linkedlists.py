from Linked_lists import singly_linkedlist

def intersection_of_LL(head1,head2):
    cur1 = head1
    cur2 = head2
    while cur1 is not None and cur2 is not None :
        cur1 = cur1.next
        cur2 = cur2.next
        if cur1.next == None :
            cur1.next = head2
            break
        elif cur2.next == None :
            cur2.next = head1
            break
    while cur1 and cur2:
        if cur1 == cur2 :
            return cur1.val
        cur1 = cur1.next
        cur2 = cur2.next.next
    return False


head1 = singly_linkedlist(1)
a = singly_linkedlist(2)
b = singly_linkedlist(3)
c = singly_linkedlist(4)
head2 = singly_linkedlist(5)
e = singly_linkedlist(6)
f = singly_linkedlist(7)
g = singly_linkedlist(8)
h = singly_linkedlist(9)


head1.next = a
a.next = b
b.next = c
c.next = head2
head2.next = e
e.next = f
f.next = g
g.next = h

result = intersection_of_LL(head1,head2)
print(result)

