#!/bin/python3

class Node:
  def __init__(self, data):
    self.data = data
    self.right = self.left = None

def preorder_traverse(node):
  if node is None:
    return
  print(node.data, end=", ")
  preorder_traverse(node.left)
  preorder_traverse(node.right)

def inorder_traverse(node):
  if node is None:
    return
  inorder_traverse(node.left)
  print(node.data, end=", ")
  inorder_traverse(node.right)

def postorder_traverse(node):
  if node is None:
    return
  postorder_traverse(node.left)
  postorder_traverse(node.right)
  print(node.data, end=", ")

root = Node("R")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

root.left = A
root.right = B

A.left = C
A.right = D

B.left = E
B.right = F

F.left = G

print("root.right.left.data:", root.right.left.data)

preorder_traverse(root)
print()
inorder_traverse(root)
print()
postorder_traverse(root)
print()
