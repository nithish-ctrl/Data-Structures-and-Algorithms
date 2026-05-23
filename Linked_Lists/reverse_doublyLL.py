from Linked_lists import Doubly_Linkedlist

def Reverse_DLL(head):
    curr = head 
    while curr : 
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    

head = Doubly_Linkedlist(3)
a=Doubly_Linkedlist(2,head)
b=Doubly_Linkedlist(5,a)
head.next=a
a.next = b
head.display_Linkedlists(head)
Reverse_DLL(head)
head.display_Linkedlists(head)
