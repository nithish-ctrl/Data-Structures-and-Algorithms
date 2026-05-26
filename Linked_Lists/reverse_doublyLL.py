from Linked_lists import Doubly_Linkedlist

def Reverse_DLL(head):
    temp = None
    curr = head 
    while curr: 
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    if temp is not None :
        head = temp.prev
    return head
    

head = Doubly_Linkedlist(3)
a=Doubly_Linkedlist(2,head)
b=Doubly_Linkedlist(5,a)
head.next=a
a.next = b
head.display_Linkedlists(head)
head = Reverse_DLL(head)
head.display_Linkedlists(head)

