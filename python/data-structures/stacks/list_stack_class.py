#!/bin/python3

"""
Stack Operations:
  Push: Adds a new element on the stack.
  Pop: Removes and returns the top element from the stack.
  Peek: Returns the top (last) element on the stack.
  isEmpty: Checks if the stack is empty.
  Size: Finds the number of elements in the stack.
"""

class Stack:
  def __init__(self, stack):
    self.stack = stack

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return self.stack.pop()
  
  def peek(self):
    return self.stack[-1]
  
  def is_empty(self):
    return not bool(self.stack)
  
  def size(self):
    return len(self.stack)

  def __str__(self):
    return self.stack

myStack = Stack(['A', 'B'])

myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())
