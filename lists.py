"""
Python Lists
a. Lists are used to store multiple items in a single variable.
b. Lists are created using square brackets.

List Items
a. List items are ordered, changeable, and allow duplicate values.
b. List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
a. When lists are ordered, it means that the items have a defined order, and that order will not change.
b. If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
The len() function is used to determine how many items a list has.
Lists contain differnt data types. That is string, int, boolean
list() function is used to create a new list 

Access Items
a. List items are accessed using their index number
b. the first inex has an index number '0'

Negative Indexing
a. Negative indexing means start from the end
b. -1 refers to the last item, -2 refers to the second last item etc.

Range of indexes
a. You can specify a range of indexes by specifying where to start and where to end the range.
b. When specifying a range, the return value will be a new list with the specified items.

Range of negative indexes
a. You can specify negative indexes if you want to start the search from the end of the list

Check if Item Exists
a. you can use the 'in' keyword to check whether a particular list item exists.

Change Item Value
To change the value of a specific item, refer to the index number.
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.

Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index.

Append Items
To add an item to the end of the list, use the append() method:

Extend List
To append elements from another list to the current list, use the extend() method.
You can use the extend() method to add any iterable object such as tuple, dictionary, sets.

Remove Specified Item
The remove() method removes the specified item.
The pop() method removes the specified index.
The del keyword also removes the specified index and removes the entire list completely
The clear() method empties the list.


Loop Through a List
You can loop through the list items by using a for loop.

Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.

Using a While Loop
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.

List Comprehension offers the shortest syntax for looping through lists:

List Comprehension
a. it offers a shorter syntax when you want to create a new list based on the values of an existing list.
b. the syntaxx for the list comprehension:
newlist = [expression for item in iterable if condition == True]
the return value is a new list, leaving the old list unchanged.
The condition is like a filter that only accepts the items that valuate to True.

The iterable can be any iterable object, like a list, tuple, set etc.
for example, you can use the 'range()' keyword to create an iterable

Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

Sort Lists:
(i) Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
To sort descending, use the keyword argument reverse = True

(ii) Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):

the str.lower method is used when you want to use a case insensitive sort function

The reverse() method reverses the current sorting order of the elements.

Copy a List
a. to copy a list, use the in-built function .copy()

Join Two Lists
a. to join two or more lists, you can use the + operator.
b. you can use the 'extend()' method to join two lists.
c. Another way to join two lists is by appending all the items from list2 into list1, one by one:



"""

#illustrations in lists

mylist = ["apple", "banana", "cherry"]
print(mylist)

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)

#list() constructor
thislist = list(("apple", "banana", "cherry")) 
print(thislist)

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#this code below prints from apple to orange
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#this returns from cherry to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#range of negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#check whether apple in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert list
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#append items in a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#removes item in a list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("while loop example")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#a short hand for creating a for loop to list all the items in the list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#newlist = [x for x in fruits if x != "apple"]
"""
newlist = [x for x in fruits]
this is a condition without an 'if' statement.
"""

newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]

#examples of expressions
newlist = [x.upper() for x in fruits]

#sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#key = fuction name.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(key = str.lower)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.reverse
print(thislist)

thislist = [100, 50, 65, 82, 23]
myList = thislist.copy()
#myList = list(thisList)
print(myList)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#join list- ex 1
list3 = list1 + list2
print(list3)
#join list- ex 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#join list- ex 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)