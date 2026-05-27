from Linked_lists import singly_linkedlist

def Length_of_loop(head):
    slow = head
    fast = head
    count = 0
    counter = 0
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            length = calculate_length(slow)
            return length
    return False

def calculate_length(meeting_point):
    temp = meeting_point
    length = 1
    while temp.next != meeting_point:
        temp = temp.next
        length+=1
    return length


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
e.next = c

print(Length_of_loop(head))



