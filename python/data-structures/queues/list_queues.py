#!/bin/python3

"""
Basic operations we can do on a queue are:
  Enqueue: Adds a new element to the queue.
  Dequeue: Removes and returns the first (front) element from the queue.
  Peek: Returns the first element in the queue.
  isEmpty: Checks if the queue is empty.
  Size: Finds the number of elements in the queue.

Reasons for using linked lists to implement queues:
  Dynamic size: The queue can grow and shrink dynamically, unlike with arrays.
  No shifting: The front element of the queue can be removed (enqueue) without having to shift other elements in the memory.

Reasons for not using linked lists to implement queues:
  Extra memory: Each queue element must contain the address to the next element (the next linked list node).
  Readability: The code might be harder to read and write for some because it is longer and more complex.
"""

queue = [5, 2, 4, 1, 3]

# enqueue
queue.append(6)
queue.append(7)

print(queue)

# dequeue
first = queue.pop(0)
second = queue.pop(1)

print(queue, first, second)

# peek
first = queue[0]

print(first)

# isEmpty
isEmpty = not bool(queue)

print(isEmpty)

# size
queue_size = len(queue)

print(queue_size)
