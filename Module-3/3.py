'''
In Python, both append() and extend() are methods used to add elements to a list, but they work differently

append()
Functionality: Adds a single element to the end of the list.

Usage: When you want to add one item (which can be a number, string, another list, etc.) to the list.
Example :

chs = ['a', 'b', 'c', 'd', 'e']
new_chs = ['f','g','h']
chs.append(new_chs)
print(chs)

Result : ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h']]

extend()
Functionality: Adds multiple elements to the end of the list by iterating over the iterable (like another list).

Usage: When you want to add elements from an iterable (like a list or a tuple) to the list.

Example :

chs = ['a', 'b', 'c', 'd', 'e']
new_chs = ['f','g','h']
chs.extend(new_chs)
print(chs)

Result : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
'''
