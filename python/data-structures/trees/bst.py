#!/bin/python3

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None
  
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=" -> ")
  inOrderTraversal(node.right)

def search(node, val):
  if node is None:
    return None # value not found
  if val == node.data:
    return node
  elif val < node.data:
    search(node.left, val)
  else:
    search(node.right, val)

def insert(node, val):
  if node is None:
    return TreeNode(val)
  else:
    if val < node.data:
      node.left = insert(node.left, val)
    elif val > node.data:
      node.right = insert(node.right, val)
  return node

def minValueNode(node):
  curr = node
  while curr.left is not None:
    curr = curr.left
  return curr

def delete(node, val):
  if node is None:
    return None
  if val < node.data:
    node.left = delete(node.left, val)
  elif val > node.data:
    node.right = delete(node.right, val)
  else:
    # if only left node
    if not node.right:
      curr = node.left
      node = None
      return curr
    
    # if only right node
    elif not node.left:
      curr = node.right
      node = None
      return curr
    
    # if both exists
    else:
      node.data = minValueNode(node.right).data
      node.right = delete(node.right, node.data)
  
  return node

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)
print("None")

# Search for a value
result = search(root, 13)
if result:
  print(f"Found the node with value: {result.data}")
else:
  print("Value not found in the BST.")

# Inserting new value into the BST
insert(root, 10)
inOrderTraversal(root)
print("None")

# Find Lowest
print("\nLowest value:",minValueNode(root).data)

# Delete node 15
delete(root,15)
inOrderTraversal(root)
print("None")
