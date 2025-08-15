#!/bin/python3

"""
1. Check the value in the center of the array.
2. If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
4. If the value is found, return the target value index. If the target value is not found, return -1.
"""

def binary_search(arr, val):
  l = 0
  r = len(arr) - 1

  while l <= r:
    m = (l + r) // 2

    if arr[m] == val:
      return m

    if arr[m] < val:
      l = m + 1
    else:
      r = m - 1

  return -1

if __name__ == "__main__":
  sorted_arr = [2, 3, 7, 7, 11, 15, 25]
  VAL = 7
  IDX = binary_search(sorted_arr, VAL)
  print(sorted_arr, f"\nval: {VAL}; index: {IDX}")
