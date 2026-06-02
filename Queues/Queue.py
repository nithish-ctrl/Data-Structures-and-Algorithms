from collections import deque
class Queue:
    def __init__(self, arr=[]):
        self.arr = deque(arr)

    def display(self):
        print(self.arr)
    
    def add(self, x):
        self.arr.append(x)
        return x
    
    def Pop(self):
        return self.arr.popleft()
    
    def Peek(self):
        return self.arr[0]

    def isEmpty(self):
        return not self.arr
    
'''
arr = [1,2,3,4,5,6]
queue = Queue(arr)
queue.display()
queue.add(2)
queue.display()
queue.Pop()
queue.display()
print(queue.Peek())
print(f"The Queue is empty : {queue.isEmpty()}")
'''
