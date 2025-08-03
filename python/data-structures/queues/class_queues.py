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

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, val):
    self.queue.append(val)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)
  
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]
  
  def isEmpty(self):
    return not bool(self.queue)
  
  def size(self):
    return len(self.queue)
  
# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
