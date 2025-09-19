#!/bin/python3

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    idx = i
    for j in range(i+1, n):
      if arr[j] < arr[idx]:
        idx = j
    arr[i], arr[idx] = arr[idx], arr[i]
  return arr

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

mylist = selection_sort(mylist)

print(mylist)
