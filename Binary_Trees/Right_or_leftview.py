from Binary_tree import TreeNode

def right_or_leftview(node):
    while node :
        print(node)
        node = node.right
    return 


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

right_or_leftview(a)