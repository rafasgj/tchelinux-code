from collections import namedtuple

class Node(namedtuple('Node','key left right')):
    pass

def bst_insert(node, key):
    if node == None:
        return Node(key, None, None)
    if key <= node.key:
        return Node(node.key, 
                    bst_insert(node.left,key), 
                    node.right)
    else: 
        return Node(node.key, 
                    node.left, 
                    bst_insert(node.right, key))

root = None
for i in range(10):
    root = bst_insert(root,i)
print(root)
