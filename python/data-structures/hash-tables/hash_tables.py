#!/bin/python3

'''
Create an empty list (it can also be a dictionary or a set).
Create a hash function.
Inserting an element using a hash function.
Looking up an element using a hash function.
Handling collisions.
'''

my_list = [[], [], [], [], [], [], [], [], [], []]

def hash_func(val):
  idx = 0
  for i in val:
    idx += ord(i)
  return idx % 10

def add(name):
  idx = hash_func(name)
  my_list[idx].append(name)

def contains(name):
  idx = hash_func(name)
  return name in my_list[idx]

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)
print("'Pete' is in the Hash Table:", contains('Pete'))
