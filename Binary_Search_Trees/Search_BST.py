from Binary_tree import TreeNode

def Search_BST(node,target):
    while node: 
        if node.val == target : return f'The target is found at {node}'
        elif node.val < target : return Search_BST(node.right, target)
        else :
            return Search_BST(node.left, target)
    return False

'''
a = TreeNode(8)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(4)
e = TreeNode(7)
f = TreeNode(10)
g = TreeNode(14)
h = TreeNode(6)
i = TreeNode(13)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
g.left = i

a.Preorder_traversal(a)
print('\r')
print(Search_BST(a, 6))
'''



