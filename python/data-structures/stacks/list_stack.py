#!/bin/python3

"""
Stack Operations:
  Push: Adds a new element on the stack.
  Pop: Removes and returns the top element from the stack.
  Peek: Returns the top (last) element on the stack.
  isEmpty: Checks if the stack is empty.
  Size: Finds the number of elements in the stack.
"""

stack = [1, 5, 2, 4, 3]

print(stack)

# push
stack.append(7)
stack.append(6)
stack.append(10)

print(stack)

# pop
first = stack.pop()
second = stack.pop()

print(stack, first, second)

# peek
print(stack[-1])

# is empty
IS_EMPTY = not bool(stack)

print(IS_EMPTY)

# size
STACK_SIZE = len(stack)

print(STACK_SIZE)
