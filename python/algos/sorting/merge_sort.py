#!/bin/python3

def merge(arr_l, arr_r):
  s_arr = []
  i, j = 0, 0
  while i < len(arr_l) and j < len(arr_r):
    if arr_l[i] <= arr_r[j]:
      s_arr.append(arr_l[i])
      i += 1
    else:
      s_arr.append(arr_r[j])
      j += 1
  s_arr.extend(arr_l[i:])
  s_arr.extend(arr_r[j:])

  return s_arr

def merge_sort(arr):
  # already sorted
  if len(arr) < 2:
    return arr
  arr_l = arr[:len(arr)//2]
  arr_r = arr[len(arr)//2:]
  s_arr_l = merge_sort(arr_l)
  s_arr_r = merge_sort(arr_r)
  return merge(s_arr_l, s_arr_r)

arr = [9, 6, 8, 7, 10, 5, 2, 4, 1, 3]
sorted_arr = merge_sort(arr)

print(sorted_arr)
