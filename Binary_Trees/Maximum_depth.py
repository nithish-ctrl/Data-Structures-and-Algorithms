from queue import Queue
from Binary_tree import TreeNode

def maximum_depth(root):
    if root is None : return 0
    q = Queue()
    q.put(root)
    level = 0
    while not q.empty():
        size = q.qsize()

        for i in range(size):
            front = q.get()
            if front.left : q.put(front.left)
            if front.right : q.put(front.right)
        level +=1 
    return level

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(7)
g = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

depth = maximum_depth(a)
print(f'The maximum depth of the binary tree is {depth}.')