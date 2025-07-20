#!/bin/python3

def bubble_sort(arr):
  counter = len(arr)
  while counter > 0:
    for i in range(1, len(arr)):
      if i == 0:
        continue
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
    
    counter -= 1
  return arr

arr = [9, 6, 8, 7, 10, 5, 2, 4, 1, 3]
sorted_arr = bubble_sort(arr)

print(sorted_arr)
