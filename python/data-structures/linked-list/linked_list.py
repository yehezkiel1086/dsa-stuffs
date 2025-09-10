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
    self.next = None
  
def traverse(head):
  curr = head
  while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
  print("null")

def findMin(head):
  minVal = head.data
  curr = head
  while curr:
    if curr.data < minVal:
      minVal = curr.data
    curr = curr.next
  return minVal

def deleteNode(head, data):
  if head.data == data:
    return head.next

  curr = head
  while curr.next and curr.next.data != data:
    curr = curr.next
  
  if curr.next == None:
    return head

  curr.next = curr.next.next

  return head

def insert(head, node, pos):
  if pos == 1:
    node.next = head
    return node

  curr = head
  for _ in range(pos - 2):
    if curr == None:
      break
    curr = curr.next
  
  node.next = curr.next
  curr.next = node

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1 = deleteNode(node1, 3)

traverse(node1)

minVal = findMin(node1)
print(minVal)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insert(node1, newNode, 2)

print("\nAfter insertion:")
traverse(node1)
