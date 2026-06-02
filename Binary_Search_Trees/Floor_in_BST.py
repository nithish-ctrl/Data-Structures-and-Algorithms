from Binary_tree import TreeNode

def Floor_in_BST(node,target):
    floor_value = -1
    while node:
        if node.val == target : 
            floor_value = node.val
            break
        elif node.val < target and node.val > floor_value:
            floor_value = node.val
            node = node.right
        elif node.val > target : 
            return Floor_in_BST(node.left, target)
        elif node.val < target : 
            return Floor_in_BST(node.right, target)
    return floor_value


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
print(Floor_in_BST(a,11))
'''         


    
