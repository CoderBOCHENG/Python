'''
Q)  What is binary search tree?
A)  Basic Rule:
    root.value > root.left.value
    root.value < root.right.value
    No duplicate value is allowed in BST
    Conlusion:
    1) BST is a sorted tree.
    2) My left subtree and my right subtree are BST as well.
'''

from binarytree import bst

root = bst()
print('BST of any height:', root)

root2 = bst(height=2)
print('BST of given height:', root2)

root3 = bst(height=2, is_perfect=True)
print('Perfect BST of given height: ', root3)
