#!/bin/python3

"""
Stack Operations:
  Push: Adds a new element on the stack.
  Pop: Removes and returns the top element from the stack.
  Peek: Returns the top (last) element on the stack.
  isEmpty: Checks if the stack is empty.
  Size: Finds the number of elements in the stack.

Reasons to implement stacks using lists/arrays:

  Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
  Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.
  A reason for not using arrays to implement stacks:

  Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, val):
    new_node = Node(val)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.val
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.val

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverse(self):
    currNode = self.head
    while currNode:
      print(currNode.val, end=" -> ")
      currNode = currNode.next
    print()

if __name__ == "__main__":
  myStack = Stack()
  myStack.push('A')
  myStack.push('B')
  myStack.push('C')

  print("LinkedList: ", end="")
  myStack.traverse()
  print("Peek: ", myStack.peek())
  print("Pop: ", myStack.pop())
  print("LinkedList after Pop: ", end="")
  myStack.traverse()
  print("isEmpty: ", myStack.isEmpty())
  print("Size: ", myStack.stackSize())
