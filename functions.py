"""
Python Functions
a. A function is a block of code which only runs when it is called.
b. You can pass data, known as parameters, into a function.
c. A function can return data as a result.

Creating a Function
a. In Python a function is defined using the def keyword:

Arguments
a. Information can be passed into functions as arguments.
b. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

Though parameters and arguments are used interchangeably, from a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition. but:
An argument is the value that is sent to the function when it is called.

Arbitary arguments(*args)
a. If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
b. This way the function will receive a tuple of arguments, and can access the items accordingly:

Keyword Arguments
a. You can also send arguments with the key = value syntax.
b. This way the order of the arguments does not matter.

Arbitary Keyword Argument(**kwargs)
a. If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
b. This way the function will receive a dictionary of arguments, and can access the items accordingly.






"""
#create a function
def my_function():
  print("Hello from a function")
my_function()  #calling a function

#arguments
def my_function(fname):
  print(fname + " Mensah")

my_function("Kofi")
my_function("Kweku")
my_function("Ama")

#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Kofi", "Mensah")
#If you try to call the function with 1 or 3 arguments, you will get an error:

#This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

#Arbitary arguments. If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#**kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
