print("Let's begin tuple")

"""
Python Tuple

a. it is used to store multiple items in a single variable. items in a tuple are ordered and unchangeable.
b. tuple is written with a brackets '()'.

Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

To determine how many items a tuple has, use the len() function:
tuple can be of any data type and can contain different data types in one tuple
the tuple() constructor can be used to create a new tuple.

Access Tuple Items
a. You can access tuple items by referring to the index number, inside square brackets:
b. Negative indexing can also be used to access tuple items. -1 refers to the last item, -2 refers to the second last item etc.

Range of Indexes
a. You can specify a range of indexes by specifying where to start and where to end the range.
b. When specifying a range, the return value will be a new tuple with the specified items.
c. To determine if a specified item is present in a tuple use the in keyword.

Update a tuple
a. Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Add Items
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

Remove items
a. items in a tuple cannot be removed. 

Python - Unpack Tuples

Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple.

Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Loop tuples
Items in a tuple can be looped through using the 'for' loop

Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.

Using a While Loop
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.





"""

#create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple when the comma is not included
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#convert tuple to a list and vice versa
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#convert to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# add a tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#remove an item in a tuple by converting it to a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#packing a tuple
fruits = ("apple", "banana", "cherry")
#Unpacking a tuple:
print("unpacking")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#loop through index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#using 'while' loops for tuples
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1