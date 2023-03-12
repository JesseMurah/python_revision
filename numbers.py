"""
Python numbers
There are three numeric types in Python, they are:
int
float
complex

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10.

Type conversion
You can convert from one type to another with the int(), float(), and complex() methods examples are shown below:

Casting in python
this is used when you want to specify a data type on a variable.
Casting in python is therefore done using constructor functions:
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


"""

x = 2    # int
y = 1.8  # float
z = 2j   # complex
x = 35e3 #float with e representing to 'the power 10'

#Type conversion
a = float(x)
b = int(y)
c = complex(x)

#Python casting
x = int(1)   # x will be 1
x = float(1)     # x will be 1.0
x = str("s1") # x will be 's1'