
class Stack:
    def __init__(self, arr=[]):
        self.arr = arr

    def Push(self, val):
        self.arr.append(val)
        return f"Pushed the element {val} in the stack {self.arr}"
    
    def Peek(self):
        return self.arr[-1]
    
    def Pop(self):
        return self.arr.pop()
    
    def isEmpty(self):
        return not self.arr
    
    def display(self):
        return self.arr

'''
mystack = Stack([2,3,4,5,6])
print(mystack.display())
print(mystack.Pop())
print(mystack.display())
print(mystack.Peek())
print(mystack.Push(129))
print(mystack.display())
'''
