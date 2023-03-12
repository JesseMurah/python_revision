"""
Python Sets
Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are written in curly braces.
Set items are unordered, unchangeable, and do not allow duplicate values.

NB: Once a set is created, you cannot change its items, but you can remove items and add new items.
Sets cannot have two items with the same value. when it happens, it will be ignored.
NB:  The values True and 1 are considered the same value in sets, and are treated as duplicates.

Accessing set items
a. You cannot access items in a set by referring to an index or a key. 
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

Add set items
a. to add one item into a set, use the 'add()' method.

Remove item(s) in a set.
To remove an item in a set, use the remove(), or the discard() method.



"""
#create a set
thisset = {"mango", "apple", "banana"}
print(thisset)

#sets cannot have two iems inn a same value
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#loop through the set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add two sets
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove item(s) in a list
thisset = {"apple", "banana", "mango"}
thisset.remove("banana")
print(thisset)