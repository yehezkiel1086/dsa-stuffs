#!/bin/python3

'''
Traversal
Remove a node
Insert a node
Sort
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.Next = None

def traverse(node):
  if node is None:
    return
  print(node.data, end=" -> ")
  traverse(node.Next)

def find_lowest(head):
  if head is None:
    return head
  curr = head
  found = head
  while curr:
    if curr.data < found.data:
      found = curr
    curr = curr.Next
  return found.data

def delete_node(head, node):
  if head is None:
    return head
  
  curr = head
  while curr.Next and curr.Next != node:
    curr = curr.Next

  if curr.Next == None:
    return head

  curr.Next = curr.Next.Next

  return head

def insert(head, node, pos):
  if pos == 1:
    node.Next = head
    return node

  if head == None:
    return head

  curr = head
  for _ in range(pos - 2):
    if curr == None:
      return head
    curr = curr.Next

  node.Next = curr.Next
  curr.Next = node

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.Next = node2
node2.Next = node3
node3.Next = node4
node4.Next = node5

traverse(node1)
print("None")
lowest = find_lowest(node1)
print("Lowest value:", lowest)
node1 = delete_node(node1, node3)
traverse(node1)
print("None")

newNode = Node(97)
node1 = insert(node1, newNode, 2)
traverse(node1)
print("None")
