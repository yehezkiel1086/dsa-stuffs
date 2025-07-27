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

class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, element):
    self.stack.append(element)
  
  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def isEmpty(self):
    return not bool(self.stack)
  
  def getSize(self):
    return len(self.stack)
  
  def __str__(self):
    return f"{self.stack}"

myStack = Stack()

# push
myStack.push("a")
myStack.push("b")
myStack.push("c")
myStack.push("d")
myStack.push("e")

print("Pushed:", myStack)

# pop
print("Popped:", myStack.pop(), myStack)

# peek
print("Peek:", myStack.peek())

# isEmpty
print("isEmpty:", myStack.isEmpty())

# getSize
print("Size:", myStack.getSize())
