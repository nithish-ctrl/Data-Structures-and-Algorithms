from Binary_tree import TreeNode

def recursive_max_depth(node):
    if node is None : return 0
    return 1 + max(recursive_max_depth(node.right), recursive_max_depth(node.right))



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

depth = recursive_max_depth(a)
print(f'The maximum depth of the binary tree is {depth}.')