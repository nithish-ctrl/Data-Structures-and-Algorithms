# Theres Singly and doubly linked lists

class singly_linkedlist():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def display_linkedlist(self, head) : 
        curr = head
        elements = []
        while curr :
            elements.append(str(curr.val))
            curr = curr.next
        print('->'.join(elements))


    def checking(self, head, value):
        curr = head
        count=1
        while curr:
            if curr.val == value : 
                print(f"Element found at position {count}")
                return True
            curr = curr.next
            count+=1
        print("Element Does not exist")
        return False
    
class Doubly_Linkedlist():
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next=next

    def display_Linkedlists(self,head):
        curr = head
        elements=[]
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print('<->'.join(elements))


'''
head = singly_linkedlist(3)
a = singly_linkedlist(2)
b = singly_linkedlist(5)

head.next = a
a.next = b

head.display_linkedlist(head)
head.checking(head, 5)



head = Doubly_Linkedlist(3)
a=Doubly_Linkedlist(2,head)
b=Doubly_Linkedlist(5,a)
head.next=a
a.next = b
head.display_Linkedlists(head)
print(head==a.prev)
'''

