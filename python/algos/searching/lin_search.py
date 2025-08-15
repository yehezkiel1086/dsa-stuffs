#!/bin/python3

"""
1. Go through the array value by value from the start.
2. Compare each value to check if it is equal to the value we are looking for.
3. If the value is found, return the index of that value.
4. If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
"""

def lin_search(arr, val):
  for i, x in enumerate(arr):
    if x == val:
      return i
  return -1

if __name__ == "__main__":
  arr = [5, 1, 4, 2, 3, 8, 7, 10, 6, 9]
  val = 7
  idx = lin_search(arr, val)
  print(arr, f"\nval: {val}; index: {idx}")
