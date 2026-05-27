
class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.right = right
        self.left = left
    
    def __str__(self) :
        return str(self.val)
    
    def Preorder_traversal(self, node): #DFS
        if not node : return
        print(node, end = "")
        self.Preorder_traversal(node.left)
        self.Preorder_traversal(node.right)
    
    def Inorder_traversal(self,node):   #DFS
        if not node : return
        self.Inorder_traversal(node.left)
        print(node, end="")
        self.Inorder_traversal(node.right)

    def Postorder_traversal(self, node):   #DFS
        if not node : return
        self.Postorder_traversal(node.left)
        self.Preorder_traversal(node.right)
        print(node, end="")
        
    
    def Levelorder_traversal(self, node):  #BFS
        pass

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

#print(a)
print(f'Preorder Traversal')
a.Preorder_traversal(a)
print(f'\nInorder Traversal')
a.Inorder_traversal(a)
print(f'\nPostorder Traversal')
a.Postorder_traversal(a)
