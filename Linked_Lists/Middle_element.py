''' 
Problem Statement: Given the head of a linked list of integers, determine the middle node of the 
linked list. However, if the linked list has an even number of nodes, return the second middle node.

'''
from Linked_lists import singly_linkedlist
def middle(head):
    curr = head
    count = 0
    element = []
    while curr:
        element.append(curr.val)
        count+=1
        curr = curr.next 
    if count % 2 == 0 :
        n = (len(element)//2) + 1  #nth element
        middle = n-1  # index 
        return element[middle]
    else :
        n = (len(element)+1)//2   #nth element
        middle = n-1  # index
        return element[middle]


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

result = middle(head)
print(result)


