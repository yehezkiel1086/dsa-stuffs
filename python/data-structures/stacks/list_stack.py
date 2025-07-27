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

# list implementation
stack = [1, 5, 2, 4, 3]

print("Original:", stack)

# push
stack.append(7)
stack.append(6)

print("Appended:", stack)

# pop
first = stack.pop()
second = stack.pop()

print("Popped:", stack, first, second)

# peek
top = stack[-1]
print("Top:", top)

# isEmpty
print("isEmpty:", not bool(stack))

# size
print("Size:", len(stack))
