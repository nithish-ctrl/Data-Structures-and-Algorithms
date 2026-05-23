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
        while curr:
            if curr.val == value : 
                print("Element found")
                return True
        return False
    

head = singly_linkedlist(3)
a = singly_linkedlist(2)
b = singly_linkedlist(5)

head.next = a
a.next = b

head.display_linkedlist(head)
head.checking(head, 4)
