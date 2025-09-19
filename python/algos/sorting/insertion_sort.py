#!/bin/python3

def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    idx = i
    key = arr.pop(idx)
    for j in range(i-1, -1, -1):
      if arr[j] > key:
        idx = j
    arr.insert(idx, key)
  return arr

arr = [64, 34, 25, 12, 22, 11, 90, 5]

arr = insertion_sort(arr)

print(arr)
