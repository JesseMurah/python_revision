"""
Python strings.
Strings in python are surrounded by either single quotation marks, or double quotation marks.
eg. 'hello' is the same as "hello" and it is displayed using a print() function.

Assign String to a Variable:
This is done by introducing the variable name followed by the equal sign and then followed by the string.
You can also introduce a multilne string into your variable by the introduction of a triple multiole quotes or triple single quotes.

Arrays:
strings in Python are arrays of bytes representing unicode characters. Square brackets can be used to access elements of the string.

String Length:
To get the length of a string, use the len() function.

Slicing:
returning a range of characters is possible by using the slice syntax. this is represented by the start index and end index, separated by the colon.
NB: the index starts from zero.

Python - Modify Strings
1. The upper() method returns the string in upper case
2. The lower() method returns the string in lower case
3. The strip() method removes any whitespace from the beginning or the end
4. The replace() method replaces a string with another string
5. The split() method splits the string into substrings if it finds instances of the separator

String contactenation
this is donr by adding two variables together by " ". But we can combine strings and numbers too by using the format() syntax.

Escape characters.
this is used to use double quotes when you normally would not be allowed. by the use of "\"
"""

print('kofi')

a = "Ama"
print(a)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = "Welcome, Kofi"
print(c[1])

d = "Welcome, Ama"
print(len(d))

e = "Welcome, Kofi"
print(e[2:4])

f = "Hello, World!"
print(f.upper())

g = "Hi, ghana!"
print(g.lower())

h = " Hello, World! "
print(h.strip())

i = "Hello, World!"
print(i.replace("H", "J"))

i1 = "Hello, World!"
print(i1.split(","))


kofiT = "Ama is going"
amaT = "to school"
print(kofiT + " " + amaT)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

txt = "We are the so-called \"Vikings\" from the north."