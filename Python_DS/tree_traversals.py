# represents an individual node in Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#In Order: Left branch, curr node, right branch
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val),
        inOrder(root.right)

#Pre Order: curr node, left branch, right branch
def preOrder(root):
    if root:
        print(root.val),
        preOrder(root.left)
        preOrder(root.right)

#Post Order: left branch, right branch, curr node
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val),

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print("Inorder traversal of binary tree is")
inOrder(root) 

print("\nPreorder traversal of binary tree is")
preOrder(root) 
  
print("\nPostorder traversal of binary tree is")
postOrder(root) 