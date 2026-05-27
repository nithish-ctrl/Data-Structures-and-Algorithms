from Linked_lists import singly_linkedlist

def Length_of_loop(head):
    slow = head
    fast = head
    count = 0
    counter = 0
    while fast and fast.next :
        if slow == fast :
            meeting_point = slow
            count+=1
            if count == 2:
                return counter
        slow = slow.next
        fast = fast.next.next
        if count == 1 :
            counter+=1
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
d.next = e
e.next = d

print(Length_of_loop(head))



