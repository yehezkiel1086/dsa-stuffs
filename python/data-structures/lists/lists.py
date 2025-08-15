#!/bin/python3

# ++ creating lists

# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

# ++ list methods
x = [9, 12, 7, 4, 11]

# Add element:
x.append(8)

# Sort list ascending:
x.sort()

print("sorted:", x)

# + create algorithms

# find lowest value
arr = [7, 12, 9, 4, 11, 8]
lowest = arr[0]

for x in arr:
	if x < lowest:
		lowest = x

print(arr, f"\nLowest: {lowest}")
