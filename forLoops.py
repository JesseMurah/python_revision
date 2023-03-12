"""
Python For Loops

a. A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
b. With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
c. The for loop does not require an indexing variable to set beforehand.

With the break statement we can stop the loop before it has looped through all the items.
With the continue statement we can stop the current iteration of the loop, and continue with the next.

Range() function
a. To loop through a set of code a specified number of times, we can use the range() function.
b. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
range(6) means values from 0 to 5. however we can specify the starting value by adding a parameter. Also we can add another specific number for the third parameter.

Else in For Loop
a. The else keyword in a for loop specifies a block of code to be executed when the loop is finished.

Nested Loops
a. A nested loop is a loop inside a loop.
b. The "inner loop" will be executed one time for each iteration of the "outer loop".

if you have a for loop without a content, you have to use the 'pass' statement to avoid an error.

"""

#print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#loop through letters
for x in "banana":
  print(x)
#exit the loop when x is banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#continue: do not print 'banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#using range() function
for x in range(6):
  print(x)
#using a start parameter
for x in range(2, 6):
  print(x)
#using the third parameter
for x in range(2, 6, 11):
  print(x)
#print all numbers from 0 to 5 & print a loop when the loop has been executed
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#pass 
for x in [0, 1, 2]:
  pass