"""
Python Conditionals
a. Python supports the usual logical conditions from mathematics:
- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
b. Python relies on identation on if-else statements unlike other programming languages.

Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Else
The else keyword catches anything which isn't caught by the preceding conditions.

The and,or and not keyword is a logical operator, and is used to combine conditional statements:

You can have if statements inside if statements, this is called nested if statements.

if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

"""

#if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#using 'and' in an if-else statement
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#using 'or' in an if-else statement
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#using 'not' in an if-else statement
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#nested if statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#using 'pass' in an if-else statement
a = 33
b = 200

if b > a:
  pass